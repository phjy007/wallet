$(document).ready(function() {
// new_artilce.html
	$("#new_article_save").click(function() {
		var username = window.location.href.split('/')[4];
		var user_id, user_uri;
		var new_article_title = $("#new_article_title").val();
		var new_article_content = $("#new_article_content").val();
		var category = ["/api/v1/category/4/"];
		$.ajax({
			type: "GET",
			url: "/api/v1/user/\?format=json\&user__username=" + username,
			async: false,
			success: function(data) {
				$.each(data, function(ii, item) {
					if(ii == "objects") {
						user_id = item[0].id;
						user_uri = item[0].resource_uri;
					}
				});
			}
		});
		var new_article_meta_data = JSON.stringify({
			"author": user_uri,
			"title": new_article_title,
			// TODO: fix this problem
			"category": ["/api/v1/category/14/"],
	        "siting_article": [],
	        "versions": [],
	        "sited_article" :[]
		});

		// Create the Article Meta for the new submission
		$.ajax({
			type: "POST",
			url: "/api/v1/article_meta/",
			contentType: 'application/json',
			data: new_article_meta_data,
			dataType: 'application/json',
			complete: function(data) {
				// for(var o in data) { alert(o); }

				// Create the first version of Article for the new Article Meta
				var new_article_meta_uri;
				$.ajax({
					type: "GET",
					async: false,
					url: "/api/v1/article_meta/\?format=json\&title=" + new_article_title,
					success: function(data) {
						$.each(data, function(i, item) {
			        		if(i == "objects") {
			        			// alert(item[0].resource_uri);
			        			new_article_meta_uri = item[0].resource_uri;
			        		}
						});
					}
				});	
				// alert(new_article_meta_uri);
				var new_article_data = JSON.stringify({
					"attachments": [],
					"comments": [],
					"content": new_article_content,
					"is_draft": false,
					"meta": new_article_meta_uri,
					"version": 0
				});
				$.ajax({
					type: "POST",
					async: false,
					url: "/api/v1/article/",
					contentType: 'application/json',
					data: new_article_data,
					dataType: 'application/json',
					success: function(data) {
						$.each(data, function(i, item) {
			        		if(i == "objects") {
			        			// alert(item[0].resource_uri);
			        			new_article_meta_uri = item[0].resource_uri;
			        		}
						});
					}
				});
				window.location.replace("/homepage/" + username);
			}
		});
	});

});
