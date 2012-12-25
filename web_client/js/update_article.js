$(document).ready(function() {
	var username = $("#nav_logo").attr("href").split('/')[2];
	var article_meta_id = window.location.href.split('/')[6];
	// var user_id, user_uri;
	var new_article_title;
	var new_article_version;
	var category = ["/api/v1/category/4/"];

	// Get article_meta's newest version number
	$.ajax({
		type: "GET",
		async: false,
		url: "/api/v1/article_meta/" + article_meta_id + "/",
		success: function(data) {
			$.each(data, function(ii, item) {
				if(ii == "versions") {
					new_article_version = item.length;
				}
				if(ii == "title") {
					new_article_title = item;
					$("#new_article_title").val(new_article_title);
				}
			});
		}
	});

	$("#new_article_save").click(function() {
		var new_article_content = $("#new_article_content").val();
		var new_article_version_data = JSON.stringify({
				"content": new_article_content,
				"meta": "/api/v1/article_meta/" + article_meta_id + "/",
				"version" : new_article_version
			});
		$.ajax({
			type: "POST",
			url: "/api/v1/article/",
			contentType: 'application/json',
			data: new_article_version_data,
			dataType: 'application/json',
			complete: function(data) {
				
			}
		});
		window.location.replace("/homepage/" + username);
		// alert(new_article_content + "\n" + ("/api/v1/article_meta/" + article_meta_id + "/") + "\n" + new_article_version);
	});

});
