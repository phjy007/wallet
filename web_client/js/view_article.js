$(document).ready(function() {
	var commentor = $("#nav_logo").attr("href").split('/')[2];
	var commentor_id;

	var article_id = window.location.href.split('/')[6];

	document.title = "Piggybank - " + commentor;

	//Load the article
	var comments, title, content, author_id, author_portrait, author_name;
	var article_versions, this_article_version;
	$.ajax({
		type: "GET",
		async: false,
		url: "/api/v1/article/" + article_id + "/",
		success: function(data) {
			$.each(data, function(ii, item) {
				if(ii == "comments") {
					comments = item;
				}
				if(ii == "content") {
					content = item;
				}
				if(ii == "meta") {
					author_id = item.author.id;
					author_portrait = item.author.portrait;
					author_name = item.author.user.username;
					title = item.title;
					article_versions = item.versions;
				}
				if(ii == "version") {
					this_article_version = item;
				}
			});
		}
	});
	$("#article_author_portrait").attr("src", "/static/" + author_portrait);
	$("#article_author_name").html(author_name);
	$("#article_title").html(title);
	$("#article_content").html(content);
	// Show the choice button for article versions
	if(this_article_version + 1 == article_versions.length) {
		$("#version_btn_label").html("View old versions");
	} else {
		$("#version_btn_label").addClass("btn-danger");
		$("#version_btn_dropdown").addClass("btn-danger");
		$("#version_btn_label").html("You're reading an old version!");
	}
	for(var i = article_versions.length - 1; i >= 0 ; i--) {
		// alert(article_versions[i].split('/')[4]);
		var version_uri = "/piggybank/" + author_name + "/article/" + article_versions[i].split('/')[4];
		$("#version_btn_start").before(
			"<li><a href=\"" + version_uri + "/\"</a>" + 
			"version " + (article_versions.length - i) +
			"</li>"
		);
	}


	// Add 'collect it!' button
	var article_author = window.location.href.split('/')[4];
	var collection_id;
	// if(article_author != commentor) {
		var has_collected = false;
		$.ajax({
			type: "GET",
			async: false,
			url: "/api/v1/collection/?belong_to__user__username=" + commentor,
			success: function(data) {
				$.each(data, function(ii, item) {
					if(ii == "objects") {
						for(var i = 0; i < item.length; i++) {
							if(item[i].article.id == article_id) {
								has_collected = true;
								collection_id = item[i].id;
								break;
							}
						}
					}
				});
			}
		});
		if(has_collected) {
			$("#collect_it_start").before(
				"<a href=\"\"><span id=\"uncollect_btn\" class=\"badge badge-success article_collect_btn\"><i class=\"icon-eye-close icon-white\"></i> uncollect it </span></a>"
			);
		} else {
			$("#collect_it_start").before(
				"<a href=\"\"><span id=\"collect_btn\" class=\"badge badge-important article_collect_btn\"><i class=\"icon-heart icon-white\"></i> collect it! </span></a>"
			);
		}
		$("#collect_btn").click(function() {
			var new_collection_data = JSON.stringify({
				"article": "/api/v1/article/" + article_id + "/",
	            "belong_to":"/api/v1/user/" + commentor_id + "/",
	            "is_private": false,
            	"keyword": [],
			});
			$.ajax({
				type: "POST",
				url: "/api/v1/collection/",
				contentType: 'application/json',
				data: new_collection_data,
				dataType: 'application/json',
				complete: function(data) {
					
				}
			});

		});
		$("#uncollect_btn").click(function() {
			$.ajax({
				type: "DELETE",
				url: "/api/v1/collection/" + collection_id + "/",
				success: function(data) {
					alert("delete successfully");
				}
			});
		});

	// } 


	// Load the comments
	var comment_item_author_name, comment_item_author_portrait, comment_item_content;
	for(var i = 0; i < comments.length; i++) {
		$.ajax({
			type: "GET",
			async: false,
			url: comments[i],
			success: function(data) {
				$.each(data, function(ii, item) {
					if(ii == "author") {
						comment_item_author_name = item.user.username;
						comment_item_author_portrait = item.portrait;
						// comment_item_author_id = item.id;
					}
					if(ii == "content") {
						comment_item_content = item;
					}
				});
			}
		});
		$("#comments_start").before(
			"<hr>" + 
			"<div class=\"row-fluid\">" +
				"<div class=\"span1\"><img class=\"img-rounded comment_portrait\" src=\"/static/" + comment_item_author_portrait + "/\"></div>" +
				"<div class=\"span11 commentor_name\"><a href=\"/piggybank/" + comment_item_author_name + "/\">" + comment_item_author_name + "</a></div>" + 
				"<div class=\"span11 comment_content\">" + comment_item_content + "</div>" + 
			"</div>" 
		);
	}


	// Load commentor's infomation
	$.ajax({
		type: "GET",
		async: false,
		url: "/api/v1/user/\?format=json\&user__username=" + commentor,
		success: function(data) {
			$.each(data, function(ii, item) {
				if(ii == "objects") {
					$("#commentor_portrait").attr("src", "/static/" + item[0].portrait);
					commentor_id = item[0].id;
				}
			});
		}
	});


	// Submit the comment
	$("#article_comment_submit").click(function() {
		var new_comment_data = JSON.stringify({
			"article": "/api/v1/article/" + article_id + "/",
            "author":"/api/v1/user/" + commentor_id + "/",
            "content": $("#article_comment").val()
		});
		$.ajax({
			type: "POST",
			url: "/api/v1/comment/",
			contentType: 'application/json',
			data: new_comment_data,
			dataType: 'application/json',
			complete: function(data) {
				
			}
		});
		location.reload();
	});

});
