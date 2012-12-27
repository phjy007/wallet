$(document).ready(function() {
	var home = window.location.href.split('/')[4];

	//Get articles
	$.ajax({
		type: "GET",
		url: "/api/v1/article_meta/\?format=json\&author__user__username=" + home,
		success: function(data) {
			$.each(data, function(i, item) {
        		if(i == "objects") {
        			var article_li_array = new Array();
        			for(var i = 0; i < item.length; i++) {
        				if(item[i].versions.length > 0) {
        					var newest_version = item[i].versions[item[i].versions.length - 1].split('/')[4];
        					$("#someone_piggybank_coins_start").after(
        						"<p><a article_uri=\"" + item[i].versions[item[i].versions.length - 1] + 
        						"\" class=\"profile_article\" href=\"/piggybank/" + home + "/article/" + 
        						newest_version  + "/\">" + item[i].title + "</a></p>"
        					);
        				}
        			}
        		}
			});
		}
	});

	//Get collections
	$.ajax({
		type: "GET",
		url: "/api/v1/collection/\?format=json\&belong_to__user__username=" + home,
		success: function(data) {
			$.each(data, function(i, item) {
        		if(i == "objects") {
        			var collection_li_array = new Array();
        			for(var i = 0; i < item.length; i++) {
        				$("#someone_piggybank_collections_start").after(
        					"<p><a href=\"/piggybank/" + home + "/collection/" + item[i].article.id  + "/\">" + 
        					item[i].article.meta.title + "</a></p>");
        			}
        		}
			});
		}
	});

	// Judge weather I am following the home
	var home_user_id;
	$.ajax({
		type: "GET",
		url: "/api/v1/user/\?format=json\&user__username=" + home,
		async: false,
		success: function(data) {
			$.each(data, function(ii, item) {
				if(ii == "objects") {
					// for(var i = 0; i < item[0].following.length; i++) {
					// 	$.ajax({
					// 		type: "GET",
					// 		url: item[0].following[i],
					// 		async: false,
					// 		success: function(data) {
					// 			alert("!!");
					// 			home_user_id = item[0].id;
					// 			// alert(home_user_id);
					// 		}
					// 	});
					// }
					home_user_id = item[0].id;
				}
			});
		}
	});
	var home_user_uri = "/api/v1/user/" + home_user_id + "/";
	var username = $("#nav_logo").attr("href").split('/')[2];
	var username_id;
	var username_following;
	var username_user_core;
	var is_following = false;
	$.ajax({
		type: "GET",
		url: "/api/v1/user/\?format=json\&user__username=" + username,
		// dataType: "application/json",
		async: false,
		success: function(data) {
			$.each(data, function(ii, item) {
				if(ii == "objects") {
					username_id = item[0].id;
					username_following = item[0].following;
					username_user_core = item[0].user.resource_uri;
					for(var i = 0; i < item[0].following.length; i++) {
						// alert(home_user_uri + " --- " + item[0].following[i]);
						if(home_user_uri == item[0].following[i]) {
							is_following = true;
							break;
						}
					}
				}
			});
		}
	});

	if(username == home) {
		$("#relationship").addClass("disabled");
		$("#relationship").removeClass("btn-warning");
		$("#relationship").removeClass("btn-success");
		$("#relationship").setClass("btn");
	}
	if(is_following) {
		$("#relationship").removeClass("btn-warning");
		$("#relationship").addClass("btn-success");
		$("#relationship").html("Unfollow");
	} else {
		$("#relationship").removeClass("btn-success");
		$("#relationship").addClass("btn-warning");
		$("#relationship").html("Follow");
	}

	$("#relationship").click(function() {
		if($("#relationship").text() == "Follow") {
			username_following[username_following.length] = home_user_uri;
			var new_username_following_data = JSON.stringify({
					"following": username_following,
					"user": username_user_core
			});
			$.ajax({
				type: "PATCH",
				url: "/api/v1/user/" + username_id + "/",
				data: new_username_following_data,
				contentType: "application/json",
				dataType: "application/json",
				success: function(data) {
					alert("haha!!");
				},
	            error : function(jqXHR, textStatus, errorThrown) {
	                //alert("The following error occured: " + textStatus, errorThrown);
	            },
	            complete : function() {
	                //alert("Venue Patch Ran");
	            }
			});
		} else if($("#relationship").text() == "Unfollow") {
			// alert(username_following);
			for(var i = 0; i < username_following.length; i++) {
				if(home_user_uri == username_following[i]) {
					username_following.splice(i, 1);
					break;
				}
			}
			// alert(username_following);
			var new_username_following_data = JSON.stringify({
					"following": username_following,
					"user": username_user_core
			});
			$.ajax({
				type: "PATCH",
				url: "/api/v1/user/" + username_id + "/",
				data: new_username_following_data,
				contentType: "application/json",
				dataType: "application/json",
				success: function(data) {
					alert("haha!!");
				},
	            error : function(jqXHR, textStatus, errorThrown) {
	                //alert("The following error occured: " + textStatus, errorThrown);
	            },
	            complete : function() {
	                //alert("Venue Patch Ran");
	            }
			});

		}
		// location.reload();
		window.location.replace(window.location.href);
	});

});

