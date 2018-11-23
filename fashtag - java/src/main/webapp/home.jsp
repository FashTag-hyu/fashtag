<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ page session="false" %>
<%@ taglib uri="http://www.springframework.org/tags" prefix="spring"%>
<html>
<head>
	<title>Home</title>
	   <script src="http://code.jquery.com/jquery-latest.js"></script> 
	<script>
	
	$(document).ready(function() {
		var imgForm = new FormData();
		
		var filename = $("#imgInp").val()
		console.log("안바꼈을때 " + filename)
		
		$("#formButton").on("click", function(){
				filename = $("#imgInp").val()
				var imgForm = new FormData();
				var imgFile = $("#imgInp")[0].files[0];
				imgForm.append("imgFile", imgFile)
// 				alert(imgFile);
// 				alert(imgForm);
					
				$.ajax({
					url:'/fashtag/insertPhoto.do',
					type:'POST',
					processData: false,
					contentType: false,
					enctype: "multipart/form-data",
					data: imgForm,
					
					success:function(data) {
						alert("분석이 완료되었습니다!");
						console.log(data);
						output = ""
						$.each(data, function(index, tag) {
							$("#output").text('')
							console.log((String)(index+1) + tag)
							if(tag == "sf") {
								output += " #"+ "봄/가을패션" + " ";							
							}
							else if(tag == "summer") {
								output += " #"+ "여름패션" + " ";
							}
							else if(tag == "winter") {
								output += " #"+ "겨울패션" + " ";
							}
							else if(tag == "date") {
								output += " #"+ "데이트룩" + " ";
							}
							else if(tag == "office") {
								output += " #"+ "오피스룩" + " ";
							}
							else if(tag == "sport") {
								output += " #"+ "운동복" + " ";
							}
							else {
								output += " #" + tag + " ";
							}
						})

						console.log(output)
						$("#output").text(output)
					},
					error:function() {
						alert("ajax통신 실패!!");
					}
					 , beforeSend: function () {
			              if($("#div_ajax_load_image").length != 0) {
			                     $("#div_ajax_load_image").css({
			                            "top": 500+"px",
			                            "left": 500+"px"
			                     });
			                     $("#div_ajax_load_image").show();
			              }
			              else {
			            	  output = '<img src="resources/load.gif" width=100 height=20 />'
			                  $("#loadPlace").html(output)
			              }

			       }
			       , complete: function () {
			                  $("#loadPlace").html("")
			       }
				});
		})
		
	})
		
	
	
        $(function() {
            $("#imgInp").on('change', function(){
                readURL(this);
            });
        });

        function readURL(input) {
            if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                    $('#blah').attr('src', e.target.result);
                }

              reader.readAsDataURL(input.files[0]);
            }
        }
	
	</script>
  <style type="text/css">
      header h1 {background: rgb(109,109,109);font-size:10pt; font-family:"맑은고딕";}
      body {background: rgb(109,109,109); font-family:"맑은고딕";border-radius:10px;
overflow-y: scroll;}
      header {text-align:center; margin:0px; padding;0px;}
      nav ul, li {list-style:none; margin:0px; padding:0px;} // 메뉴 바 사이 간격 없애려면 이거 그냥 주석처리하기
      article {background-color:#FFFFFF;color:#58521E; display:block; width:70%; border-radius:10px; float:left; margin:10px; padding:5px;text-align:right;}
      section {background-color:#FFFFFF; border-radius:0px; margin:0px; padding:50px; text-align:center;}
      h1, a:link, a:visited, nav {color:#4C4C4C; text-decoration:none;} 
      .menubar{border:none; border:0px; margin:0px; padding:0px; font: 67.5% "Lucida Sans Unicode", "Bitstream Vera Sans", "Trebuchet Unicode MS", "Lucida Grande", Verdana, Helvetica, sans-serif; font-size:20px; font-weight:bold;}
      .menubar ul{background: rgb(109,109,109); height:80px; list-style:none; margin:0; padding:0;}
      .menubar li{float:left; padding:0px;}
      .menubar li a{background: rgb(109,109,109); color:#cccccc; display:block; font-weight:normal; line-height:80px; margin:0px; padding:0px 40px; text-align:center; text-decoration:none;}
      .menubar li a:hover, .menubar ul li:hover a{background: rgb(71,71,71); color:#FFFFFF; text-decoration:none;}
      .menubar li ul{background: rgb(109,109,109); display:none; height:auto; padding:0px; margin:0px; border:0px; position:absolute; width:200px; z-index:200;}
      .menubar li:hover ul{display:block;}
      .menubar li li {background: rgb(109,109,109); display:block; float:none; margin:0px; padding:0px; width:200px;}
      .menubar li:hover li a{background:none;}
      .menubar li ul a{display:block; height:80px; font-size:20px; font-style:normal; margin:0px; padding:0px 10px 0px 15px; text-align:left;}
      .menubar li ul a:hover, .menubar li ul li:hover a{background: rgb(71,71,71); border:0px; color:#ffffff; text-decoration:none;}
      .menubar p{clear:left;}
      .foodimage {float:left;}
      .wrap {
marin: 0 auto;
}

      ul.tabs {width: 1000px;height: 80px;
margin: 0 auto;
list-style: none;overflow: hidden;
 padding: 0;
}

      ul.tabs li {float: left; 
width: 130px;


}

      ul.tabs li a {
position: relative;
 display: block;
height: 30px;
margin-top: 40px;
padding: 10px 0 0 0;
font-family: 'Open Sans', sans-serif;
 font-size: 18px;
 text-align: center; text-decoration: none;
 color: #ffffff;
 background: #6edeef;
 -webkit-box-shadow: 8px 12px 25px 2px rgba(0,0,0,0.4);
 -moz-box-shadow: 8px 12px 25px 2px rgba(0,0,0,0.4);
 box-shadow: 8px 12px 25px 2px rgba(0,0,0,0.4);
border: 0px solid #000000;
-webkit-transition: padding 0.2s ease, margin 0.2s ease;
 -moz-transition: padding 0.2s ease, margin 0.2s ease;
 -o-transition: padding 0.2s ease, margin 0.2s ease;
  -ms-transition: padding 0.2s ease, margin 0.2s ease;
  transition: padding 0.2s ease, margin 0.2s ease;
}

      .tabs li:first-child a {
z-index: 3;
  -webkit-border-top-left-radius: 8px;
-moz-border-radius-topleft: 8px;
border-top-left-radius: 8px;
}

      .tabs li:nth-child(2) a {
z-index: 2;
}

      .tabs li:last-child a {
z-index: 1;
  -webkit-box-shadow: 2px 8px 25px -2px rgba(0,0,0,0.3);
 -moz-box-shadow: 2px 8px 25px -2px rgba(0,0,0,0.3);
 box-shadow: 2px 8px 25px -2px rgba(0,0,0,0.3);
  -webkit-border-top-right-radius: 8px;
-moz-border-radius-topright: 8px;
border-top-right-radius: 8px;
}

      ul.tabs li a:hover {
margin: 35px 0 0 0;
   padding: 10px 0 5px 0;
}

      ul.tabs li a.active {
margin: 30px 0 0 0;
   padding: 10px 0 10px 0;
background: #545f60;
 color: #6edeef;
/*color: #ff6831;*/
   z-index: 4;
outline: none;
}

      .group:before,
.group:after {
 content: " "; /* 1 */
    display: table; /* 2 */
}

      .group:after {
 clear: both;
}

      #content {padding:10px; 
width: 1000px;
  height: 1000px;  margin: 0 auto;
  background: #BDBDBD; 
-webkit-box-shadow: 2px 8px 25px -2px rgba(0,0,0,0.3);
 -moz-box-shadow: 2px 8px 25px -2px rgba(0,0,0,0.3);
 box-shadow: 2px 8px 25px -2px rgba(0,0,0,0.3);
  -webkit-border-bottom-right-radius: 8px;
-webkit-border-bottom-left-radius: 8px;
-moz-border-radius-bottomright: 8px;
-moz-border-radius-bottomleft: 8px;
border-bottom-right-radius: 8px;
border-bottom-left-radius: 8px;
}
      span {
font-family: 'Open Sans', sans-serif;
  padding: 30px 40px;
  color: #ffffff;
  line-height: 26px;
  font-size: 18px;
  margin: 0;
}

      #one {
  
}
#two {
  
}
#three {
  
}
      #sports {width:60%; height:200px; margin:auto; text-align:center;}
      #sportsSec {width: 1000px; height:450px; margin:0 auto; padding:10px; background: #BDBDBD; 
-webkit-box-shadow: 2px 8px 25px -2px rgba(0,0,0,0.3);
 -moz-box-shadow: 2px 8px 25px -2px rgba(0,0,0,0.3);
 box-shadow: 2px 8px 25px -2px rgba(0,0,0,0.3);
  -webkit-border-bottom-right-radius: 8px;
-webkit-border-bottom-left-radius: 8px;
-moz-border-radius-bottomright: 8px;
-moz-border-radius-bottomleft: 8px;
border-bottom-right-radius: 8px;
border-bottom-left-radius: 8px;font-family: 'Open Sans', sans-serif; color: #ffffff;
 font-size: 18px;
 
}
   </style>
</head>
<body>

   <header><h1><a id="1" href="/"><img src="resources/logo.JPG" width="800" height=170"/></a></h1>
   <div class="menubar">
   <ul>
    <li><a href="/">Home</a></li>
    <li><a href="home.html" id="current">Info</a>
   <ul>
        <li><a href="home.html">Fashion Tag</a></li>
        <li><a href="home.html">How to do</a></li>
       </ul>
    </li>
   </ul>
   </div>
   </header>
 <article>
  <section>
  <div class="wrap">

  
  <ul class="tabs group">
    <li><a class="active" href="#/one">MY TAG</a></li>
    <li><a href="#/two">Training</a></li>
  </ul>

  
  <div id="content">
    <span id="one"></br></br><img src="resources/title2.JPG" width="550" height=50"/></br></br>
    <form id="form1" runat="server" id="photo" action="movePhoto.do" method="post" enctype="multipart/form-data">
        <img id="blah" src="#" alt="사진을 업로드하세요" height="500", width="400"/><br/><br/><br/>
        <input type='file' id="imgInp" name="imgfile"/>
        <input type="button" id="formButton" value="해쉬태그">
		</br></br><div id="loadPlace"></div></br></br>
		<textarea rows="9" cols="70" id="output" name="contents" style="text-align:center; letter-spacing:3px" placeholder="패션 태그 결과가 나옵니다."></textarea>
		<input type="submit" id="finish" value="완료!">
    </form>
    </span>
  </section>
  
</div>
 	

</body>
</html>
