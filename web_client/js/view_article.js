$(document).ready(function() {
	var commentor = window.location.href.split('/')[4];
	var commentor_id;

	var article_id = window.location.href.split('/')[6];

	document.title = "Piggybank - " + commentor;

	//Load the article
	var comments, title, content, author_id, author_portrait, author_name;
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
				}
			});
		}
	});
	$("#article_author_portrait").attr("src", "/static/" + author_portrait);
	$("#article_author_name").html(author_name);
	$("#article_title").html(title);
	$("#article_content").html(content);

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
				"<div class=\"span11 commentor_name\"><a>" + comment_item_author_name + "</a></div>" + 
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
		window.location.replace(window.location.href);
	});

});
