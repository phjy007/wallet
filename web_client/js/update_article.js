$(document).ready(function() {
	var username = $("#nav_logo").attr("href").split('/')[2];
	var article_meta_id = window.location.href.split('/')[6];
	// var user_id, user_uri;
	var new_article_title;
	var new_article_version;
	var category = ["/api/v1/category/4/"];

	var reference_article_metas = new Array();


	// Get article_meta's newest version number and load references
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
				if(ii == "siting_article") {
					reference_article_metas = item;
				}
			});
		}
	});
	alert(reference_article_metas);	

	
	//Show the referenced article metas
	for(var i = 0; i < reference_article_metas.length; i++) {
		var saved_reference_article_title, saved_reference_article_lastest_version;
		$.ajax({
			type: "GET",
			async: false,
			url: reference_article_metas[i],
			success: function(data) {
				$.each(data, function(ii, item) {
					if(ii == "versions") {
						saved_reference_article_lastest_version = item[item.length - 1].split("/")[4];
					}
					if(ii == "title") {
						saved_reference_article_title = item;
					}
				});

			}
		});
		$("#add_references_starts").before(
			"<div id=\"ref_article_" + saved_reference_article_lastest_version + "\" class=\"reference_item\">" + saved_reference_article_title + 
			"&nbsp&nbsp&nbsp&nbsp<a id=\"remove_ref_article_" + saved_reference_article_lastest_version + 
			"\" href=\"#\"><i class=\"icon-remove-sign\"></i></a></div>" 
		);
		$("#remove_ref_article_" + saved_reference_article_lastest_version).click(function() {
			alert(this);
			var delete_div_id = "ref_article_" + saved_reference_article_lastest_version;
			$("#" + delete_div_id).remove();
			for(var iii = 0; iii < reference_article_metas.length; iii++) {
				

				// alert(reference_article_metas[iii] + "   " + reference_article_metas[i]);
				if(reference_article_metas[iii] == reference_article_metas[i]) {
					reference_article_metas.splice(iii, 1);
				}
			}
		});
	}



	//add references
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
									// alert(reference_article_metas[i]);
							// }			
							alert(reference_article_metas);				
						}
					});
				},
				error: function(data) {
					alert("No article id " + reference_article_id);
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
