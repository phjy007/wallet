$(document).ready(function(){
	var username = window.location.href.split('/')[4];
	$("#username").html(username);

	// Get user infomation
	$.ajax({
		type: "GET",
		url: "/api/v1/user/" + username + "/",
		success: function(data) {
			$.each(data, function(i, item) {
        		if(i == "fans") {
        			$("#fans").html(item.length);
        		}
        		if(i == "following") {
        			$("#following").html(item.length);
        		}
			});
		}
	});

	// Get user articles(meta)
	$.ajax({
		type: "GET",
		url: "/api/v1/article_meta/" + username + "/",
		success: function(data) {
			$.each(data, function(i, item) {
        		if(i == "objects") {
        			var article_li_array = new Array();
        			for(var i = 0; i < item.length; i++) {
        				article_li_array[i] = "<li><a href=\"" + item[i].versions[item[i].versions.length - 1] + "\">" + item[i].title + "</a></li>";
        			}
        		}
        		$("#my_coins").after(article_li_array);
			});
		}
	});

	// Get user collection
	$.ajax({
		type: "GET",
		url: "/api/v1/collection/" + username + "/",
		success: function(data) {
			$.each(data, function(i, item) {
        		if(i == "objects") {
        			var collection_li_array = new Array();
        			for(var i = 0; i < item.length; i++) {
        				collection_li_array[i] = "<li><a href=\"" + item[i].article.resource_uri + "\">" + item[i].article.meta.title + "</a></li>";
        			}
        		}
        		$("#my_collection").after(collection_li_array);
			});
		}
	});		

	// Get feedevent in inbox
	// $.ajax({
	// 	type: "GET",
	// 	url: "/api/v1/inbox/" + username + "/",
	// 	success: function(data) {
	// 		// alert( "Data Saved: " + data);
	// 		$.each(data, function(i, item) {
//           		if(i == "feed_event") {
//           			for(var i = 0; i < item.length; i++) {
//           				// alert(item[i]);

//           			}
//           		}
//     				});
	// 	}
	// });

});