$(document).ready(function() {
	var username = window.location.href.split('/')[4];
	$("#username").html(username);
	document.title = "Piggybank - " + username
	// Get user infomation and render the user's homepage
	$.ajax({
		type: "GET",
		url: "/api/v1/user/\?format=json\&user__username=" + username,
		success: function(data) {
			$.each(data, function(ii, item) {
				if(ii == "objects") {
					$("#profile_followers").html(item[0].fans.length);
					$("#profile_following").html(item[0].following.length);
					$("#profile_portrait").attr("src", "/static/" + item[0].portrait);
				}
			});
		}
	});

	// Get user articles(meta)
	$.ajax({
		type: "GET",
		url: "/api/v1/article_meta/\?format=json\&author__user__username=" + username,
		success: function(data) {
			$.each(data, function(i, item) {
        		if(i == "objects") {
        			var article_li_array = new Array();
        			for(var i = 0; i < item.length; i++) {
        				if(item[i].versions.length > 0) {
        					var newest_version = item[i].versions[item[i].versions.length - 1].split('/')[4];
        					$("#my_coins").after("<li><a article_uri=\"" + item[i].versions[item[i].versions.length - 1] + "\" class=\"profile_article\" href=\"/piggybank/" + username + "/article/" + newest_version  + "/\">" + item[i].title + "</a></li>");
        				}
        			}
        		}
			});
		}
	});

	// Get user collection
	$.ajax({
		type: "GET",
		url: "/api/v1/collection/\?format=json\&belong_to__user__username=" + username,
		success: function(data) {
			$.each(data, function(i, item) {
        		if(i == "objects") {
        			var collection_li_array = new Array();
        			for(var i = 0; i < item.length; i++) {
        				$("#my_collection").after("<li><a href=\"/piggybank/" + username + "/collection/" + item[i].article.id  + "/\">" + item[i].article.meta.title + "</a></li>");
        			}
        		}
			});
		}
	});

	//Get feedevent in inbox
	$.ajax({
		type: "GET",
		// url: "/api/v1/feedevent/" + username + "/",
		url: "/api/v1/feedevent/\?format=json\&inbox__user__user__username=" + username,
		success: function(data) {
			$.each(data, function(i, item) {
				if(i == "objects") {
					for(var i = 0; i < item.length ; i++) {
						if(item[i].article != null) {
							var author = item[i].article.meta.author.user.username;
							var article_id = item[i].article.resource_uri.split('/')[4];
							var title = item[i].article.meta.title;
							var action = item[i].action;
							var time = item[i].time;
							var content_preview = item[i].article.content;
							var protrait = item[i].article.meta.author.portrait;
							$("#feedevent_start").before(
								"<div>" +
									"<div class=\"row-fluid\">" +
										"<div class=\"span1\">" +
											"<a href=\"/piggybank/" + author + "\">" +
												"<img class=\"feedevent_portrait img-rounded\" src=\"/static/" + protrait + "\">" +
											"</a>" +
										"</div>" +
										"<div class=\"span11\">" +
											"<a href=\"/piggybank/" + author + "\"><span>" + author + " </span></a>" +
											"<span>" + action + "s&nbsp </span>" +
											"<a href=\"/piggybank/" + author + "/article/" + article_id + "/\"><b>" + title + "</b></a>" +
											"<div class=\"wallet_assist_word\">" + content_preview + "</div>" +
											"<div class=\"pull-right comment_and_collect\">" +
												"<span class=\"feed_event_time\"><i class=\"icon-time\"></i> " + time + "</span>" +
											"</div>" +
											// "<div class=\"pull-right comment_and_collect\">" +
											// 	"<a href=\"#\"><span class=\"badge label-info\"><i class=\"icon-pencil icon-white\"></i>Comment</span></a>" +
											// 	"&nbsp &nbsp " +
											// 	"<a href=\"#\"><span class=\"badge badge-important\"><i class=\"icon-heart icon-white\"></i>Collect</span></a>" +
											// "</div>" +
										"</div>" +
									"</div>" +
								"</div>" +						
								"<hr>"
							);
						} else if(item[i].collection != null) {
							// alert(item[i].collection);
							var author = item[i].collection.article.meta.author.user.username;
							var collector = item[i].collection.belong_to.user.username;
							var article_id = item[i].collection.article.resource_uri.split('/')[4];
							var title = item[i].collection.article.meta.title;
							var time = item[i].time;
							var portrait = item[i].collection.belong_to.portrait;
							$("#feedevent_start").before(
								"<div>" +
									"<div class=\"row-fluid\">" +
										"<div class=\"span1\">" +
											"<a href=\"/piggybank/" + collector + "\">" +
												"<img class=\"feedevent_portrait img-rounded\" src=\"/static/" + portrait + "\">" +
											"</a>" +
										"</div>" +
										"<div class=\"span11\">" +
											"<a href=\"/piggybank/" + collector + "\"><span>" + collector + " </span></a>" +
											"<span>collects </span>" +
											"<a href=\"/piggybank/" + author + "\"><span>" + author + "'s </span></a>" +
											"<a href=\"/piggybank/" + collector + "/collection/" + article_id + "/\"><b>" + title + "</b></a>" +
											"<div class=\"wallet_assist_word\">This article will tell you something about Linux Driver Programming...</div>" +
											"<div class=\"pull-right comment_and_collect\">" +
												"<span class=\"feed_event_time\"><i class=\"icon-time\"></i> " + time + "</span>" +
											"</div>" +
											// "<div class=\"pull-right\">" +
											// 	"<a href=\"#\"><span class=\"badge label-info\"><i class=\"icon-pencil icon-white\"></i>Comment</span></a>" +
											// 	"&nbsp &nbsp " +
											// 	"<a href=\"#\"><span class=\"badge badge-important\"><i class=\"icon-heart icon-white\"></i>Collect</span></a>" +
											// "</div>" +
										"</div>" +
									"</div>" +
								"</div>" +						
								"<hr>"
							);
						}
					}
				}
			});
			$("#feedevent_start").before("</ul>");
		}
	});
	
	// Get user infomation and render the user's homepage
	$("#dropdown_profile").click(function() {
		var username = window.location.href.split('/')[4];
		$("#profile_window_username").html(username);
		document.title = "Piggybank - " + username
		$.ajax({
			type: "GET",
			url: "/api/v1/user/\?format=json\&user__username=" + username,
			success: function(data) {
				$.each(data, function(ii, item) {
					if(ii == "objects") {
						$("#profile_window_portrait").attr("src", "/static/" + item[0].portrait);
						$("#profile_window_email").attr("value", item[0].user.email);
					}
				});
				$("#nav_logo").attr("href", "/homepage/" + username);
			}
		});
	});

	$("#profile_window_save").click(function() {
		var username = window.location.href.split('/')[4];
		var new_email = $("#profile_window_email").val();
		var new_pwd = $("#profile_window_password").val();
		var new_pwd_again = $("#profile_window_password_again").val();
		// TODO: to check weather the new_pwd is a null string
		if(new_pwd != new_pwd_again) {
			alert("Please confirm your new password.");
			$("#profile_window_password").val("");
			$("#profile_window_password_again").val("");
		} else if(new_email == "") {
			alert("Please confirm your new e-mail address.");
		} else {
			$.ajax({
				type: "PATCH",
				url: "/api/v1/user/2/",
				contentType: "application/json",
				data: '{ "nickname": "TT#OOO#MM"}',
				dataType: "application/json",
				processData:  false,
				success: function(data) {
					alert("success");
				}
			});
		}
		location.reload();
	});


	// Set the unread message mark
	$.ajax({
		type: "GET",
		url: "/api/v1/message/\?format=json\&to_user__user__username=" + username,
		success: function(data) {
			$.each(data, function(ii, item) {
				if(ii == "objects") {
					var unread_msg_count = 0;
					for(var i = 0; i < item.length; i++) {
						if(!item[i].has_read)
							unread_msg_count++;
					}
					if(unread_msg_count > 0) {
						$("#nav_message").append("<b style=\"color:red;\"> (" + unread_msg_count + ")</b>");
						$("#dropdown_message").append("<b style=\"color:red;\"> (" + unread_msg_count + ")</b>");

					}
				}
			});
		}
	});

	// User's following window
	$("#profile_following").click(function() {
		var username = window.location.href.split('/')[4];
		$("#followingModal .modal-body").empty();
		$("#followingModal .modal-body").append(
			"<div id=\"followingModal_start\"></div>"
		);
		$.ajax({
			type: "GET",
			url: "/api/v1/user/\?format=json\&user__username=" + username,
			success: function(data) {
				$.each(data, function(ii, item) {
					if(ii == "objects") {
						// var following_array = new Array();
						for(var i = 0; i < item[0].following.length; i++) {
							$.ajax({
								type: "GET",
								url: item[0].following[i],
								success: function(data) {
									var name, portrait, email;
									$.each(data, function(j, jtem) {
										if(j == "user") {
											name = jtem.username;
											email = jtem.email;
										}
										if(j == "portrait") {
											portrait = jtem;
										}
									});
									$("#followingModal_start").before(
											"<div class=\"profile_following_item\">" +
											"<img class=\"img-rounded profile_following_img\" src=\"/static/" + portrait + "\">"+
											"<span><a href=\"/piggybank/"+ name + "/\">" + name + "</a><span> " + email + "</span></span>" + 
											"<hr>" +
											"</div>"
									);
								}
							});
						}
					}
				});
			}
		});
	});


	// User's followers window
	$("#profile_followers").click(function() {
		var username = window.location.href.split('/')[4];
		$("#followersModal .modal-body").empty();
		$("#followersModal .modal-body").append(
			"<div id=\"followersModal_start\"></div>"
		);
		$.ajax({
			type: "GET",
			url: "/api/v1/user/\?format=json\&user__username=" + username,
			success: function(data) {
				$.each(data, function(ii, item) {
					if(ii == "objects") {
						// var following_array = new Array();
						for(var i = 0; i < item[0].fans.length; i++) {
							$.ajax({
								type: "GET",
								url: item[0].fans[i],
								success: function(data) {
									var name, portrait, email;
									$.each(data, function(j, jtem) {
										if(j == "user") {
											name = jtem.username;
											email = jtem.email;
										}
										if(j == "portrait") {
											portrait = jtem;
										}
									});
									$("#followersModal_start").before(
											"<div class=\"profile_followers_item\">" +
											"<img class=\"img-rounded profile_followers_img\" src=\"/static/" + portrait + "\">"+
											"<span><a href=\"/piggybank/"+ name + "/\">" + name + "</a><span>  " + email + "</span></span>" + 
											"<hr>" +
											"</div>"
									);
								}
							});
						}
					}
				});
			}
		});
	});



});

