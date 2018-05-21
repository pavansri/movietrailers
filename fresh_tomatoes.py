#!/usr/bin/env python
import webbrowser
import os
import re


main_page_head = '''
<!DOCTYPE html>
<html>
<head >
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>Movie trailers</title>

   <style>

    .modal {
    display: none; /* Hidden by default */
    position: fixed; /* Stay in place */
    z-index: 1; /* Sit on top */
    padding-top:100px;
    left: 0;
    top: 0;
    width: 100%; /* Full width */
    height: 100%; /* Full height */
    overflow: auto; /* Enable scroll if needed */
    background-color: rgb(0,0,0); /* Fallback color */
    background-color: rgba(0,0,0,0.1); /* Black w/ opacity */
}

/* Modal Content/Box */
.modal-content {
    margin: 5% auto; /* 5% from the top and centered */
    padding: 20px;
    width: 560px; /* Could be more or less, depending on screen size */
    min-height:500px;
}

/* The Close Button */
.close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
}

.close:hover,
.close:focus {
    background-color: black;
    text-decoration: none;
    cursor: pointer;
    padding-left:5px;
    padding-right:5px;
}

      .container{
        display: flex;
        flex-wrap:wrap;
        font-family:arial,cursive;
    background:#191919;
       }
     .box{
          width:100%;
          min-height:150px;
          cursor:pointer;
        }
      @media screen and (min-width :450px)  {
      .m1:hover,.m2:hover,.m3:hover,.m4:hover{
             border:1px;
             background-color:    #8c8c8c;
    border-radius:20px;
             }

       .m1{width:50%;}
       .m2{width:50%;}
       .m3{width:50%;}
       .m4{width:50%;}
       h1 {background-color:black;}
        }
      h1 {background-color:black;
         font-family:arial,cursive;}
      </style>
</head>
      <div>
      <!-- The Modal -->
         <div id="myModal" class="modal" >

  <!-- Modal content -->
           <div class="modal-content">
                <span class="close">&times;</span>
                 <iframe id="f" width="560" height="315"
                 {movie_tiles} src="" frameborder="0" allow="autoplay;
                 encrypted-media" allowfullscreen></iframe>
        </div>

        </div>
</div>
<script>
   // Get the modal
var modal = document.getElementById('myModal');

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
    onc = function(c) {
    modal.style.display = "block";
    c='https://www.youtube.com/embed/'+c;
    console.log(c);
    document.getElementById("f").setAttribute("src",c);
}

// When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
}
span.onclick = function(){
            console.log("hello");
            var iframe = document.getElementById("f");
            iframe.src = iframe.src;
            modal.style.display = "none";
        }


// When the user clicks anywhere outside of the modal, close it
   window.onclick = function(event) {
       if (event.target == modal) {
          modal.style.display = "none";
    }
}
</script>

</head>
'''

# The main page layout and title bar
main_page_content = '''
<body style="text-align:center">
   <h1 style="color:white">MOVIE TRAILERS</h1>
   <div class="container">

        <div class="box m1" onclick="onc('BoohRoVA9WQ')">
            <img vspace="30"src="https://bit.ly/2KGr1EB"
                style="width:60%"height="600" hspace="30";>
                    <h2 style="color:#191919;">Ironman2</h2></div>

        <div class="box m2" onclick="onc('6ZfuNTqbHE8')">
            <img vspace="30"src="https://bit.ly/2kb1UOJ"
                style="width:60%"height="600" hspace="30">
                     <h2 style="color:#191919;">Avengers</h2></div>

        <div class="box m3" onclick="onc('xnv__ogkt0M')">
            <img vspace="30"src="https://bit.ly/2GB4vKH"
                style="width:60%" height="600" hspace="30">
                    <h2 style="color:#191919;">Civil War</h2>  </div>

        <div class="box m4" onclick="onc('ue80QwXMRHg')">
            <img vspace="30"src="https://bit.ly/2wVfGys"
                style="width:60%"height="600"  hspace="30">
                    <h2 style="color:#191919;">Thor</h2></div>

</body>
</html>
'''

movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-title text-center"
data-trailer-youtbe-id="{trailer_youtube_id}" data-toggle="modal"
data-target="#trailer">
     <img src="{poster_image_url}" width="220" height="342">
     <h2 style="color:white;">{movie_title}</h2>
    </div>
'''


def create_movie_tiles_content(movies):
    content = ''
    for movie in movies:
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
         )
        return content


def open_movies_page(movies):
    output_file = open('fresh_tomatoes.html', 'w')
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    output_file.write(main_page_head+rendered_content)
    output_file.close()

    url = os.path.abspath(output_file.name)
    webbrowser.open('file://'+url, new=2)
