$(document).ready(function() {
	var reference_article_metas = new Array();
	var new_reference_article_uri;
	// add references
	$("#add_references_btn").click(function() {
		var reference_article_id = $("#add_references_input").val();
		if(reference_article_id != "") {
			new_reference_article_uri = "/api/v1/article/" + reference_article_id + "/";
			// alert(new_reference_article_uri);
			$.ajax({
				type: "GET",
				url: new_reference_article_uri,
				async: false,
				success: function(data) {
					$.each(data, function(ii, item) {
						var reference_article_title;
						if(ii == "meta") {
							reference_article_title = item.title;
							var new_reference_uri = "/api/v1/article_meta/" + item.id + "/";
							// alert(new_reference_uri);
							var ref_exist = false;
							for(var i = 0; i < reference_article_metas.length; i++) {
								if(reference_article_metas[i] == new_reference_uri) {
									ref_exist = true;
									break;
								}
							}
							// alert("ref_exist=" + ref_exist);
							if(!ref_exist) {
								reference_article_metas.push(new_reference_uri);
								$("#add_references_starts").before(
									"<div id=\"ref_article_" + reference_article_id + "\" class=\"reference_item\">" + reference_article_title + 
									"&nbsp&nbsp&nbsp&nbsp<a id=\"remove_ref_article_" + reference_article_id + "\" href=\"#\"><i class=\"icon-remove-sign\"></i></a></div>" 
								);
								$("#remove_ref_article_" + reference_article_id).click(function() {
									var delete_div_id = "ref_article_" + reference_article_id;
									$("#" + delete_div_id).remove();
									for(var i = 0; i < reference_article_metas.length; i++) {
										if(reference_article_metas[i] == new_reference_uri) {
											reference_article_metas.splice(i, 1);
										}
									}
								});
							} else {
									alert("EXISTS!");
							}
							// for(var i = 0; i < reference_article_metas.length; i++) {
							// 		alert(reference_article_metas[i]);
							// }							
						}
					});
				},
				error: function(data) {
					alert("No article id " + reference_article_id);
				}
			});
		}
	});

	// save a new article
	$("#new_article_save").click(function() {
		var username = $("#nav_logo").attr("href").split('/')[2];
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
		// alert(reference_article_metas);
		var new_article_meta_data = JSON.stringify({
			"author": user_uri,
			"title": new_article_title,
			// TODO: fix this problem
			"category": ["/api/v1/category/1/"],
	        "siting_article": reference_article_metas,
	        "versions": [],
	        "sited_article" : []
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
				// Create the first version for the new Article Meta
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
