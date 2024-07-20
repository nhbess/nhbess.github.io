---
layout: post
title: An unexpected fractal
image: /assets/images/post_pics/An unexpected fractal/18.jpg
---

Some time ago I wrote a program for visualizing search algorithms in a grid. A relatively simple [Breadth first search](https://en.wikipedia.org/wiki/Breadth-first_search)that mutate its color on each search depth over a grid.

Nice plots. Extremely slow.
<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
  <img src="assets/images/post_pics/An unexpected fractal/0.jpg" alt="Image 1" style="width: 100%; max-width: 200px; max-height: 200px; object-fit: cover;">   
  <img src="assets/images/post_pics/An unexpected fractal/1.jpg" alt="Image 2" style="width: 100%; max-width: 200px; max-height: 200px; object-fit: cover;">   
  <img src="assets/images/post_pics/An unexpected fractal/10.jpg" alt="Image 3" style="width: 100%; max-width: 200px; max-height: 200px; object-fit: cover;">  
  <img src="assets/images/post_pics/An unexpected fractal/11.jpg" alt="Image 4" style="width: 100%; max-width: 200px; max-height: 200px; object-fit: cover;">  
  <img src="assets/images/post_pics/An unexpected fractal/12.jpg" alt="Image 5" style="width: 100%; max-width: 200px; max-height: 200px; object-fit: cover;">  
  <img src="assets/images/post_pics/An unexpected fractal/13.jpg" alt="Image 6" style="width: 100%; max-width: 200px; max-height: 200px; object-fit: cover;">  
  <img src="assets/images/post_pics/An unexpected fractal/14.jpg" alt="Image 7" style="width: 100%; max-width: 200px; max-height: 200px; object-fit: cover;">  
  <img src="assets/images/post_pics/An unexpected fractal/15.jpg" alt="Image 8" style="width: 100%; max-width: 200px; max-height: 200px; object-fit: cover;">  
  <img src="assets/images/post_pics/An unexpected fractal/16.jpg" alt="Image 9" style="width: 100%; max-width: 200px; max-height: 200px; object-fit: cover;">  
  <img src="assets/images/post_pics/An unexpected fractal/17.jpg" alt="Image 10" style="width: 100%; max-width: 200px; max-height: 200px; object-fit: cover;"> 
  <img src="assets/images/post_pics/An unexpected fractal/18.jpg" alt="Image 11" style="width: 100%; max-width: 200px; max-height: 200px; object-fit: cover;"> 
  <img src="assets/images/post_pics/An unexpected fractal/19.jpg" alt="Image 12" style="width: 100%; max-width: 200px; max-height: 200px; object-fit: cover;"> 
  <img src="assets/images/post_pics/An unexpected fractal/2.jpg" alt="Image 13" style="width: 100%; max-width: 200px; max-height: 200px; object-fit: cover;">  
  <img src="assets/images/post_pics/An unexpected fractal/3.jpg" alt="Image 14" style="width: 100%; max-width: 200px; max-height: 200px; object-fit: cover;">  
  <img src="assets/images/post_pics/An unexpected fractal/4.jpg" alt="Image 15" style="width: 100%; max-width: 200px; max-height: 200px; object-fit: cover;">  
  <img src="assets/images/post_pics/An unexpected fractal/5.jpg" alt="Image 16" style="width: 100%; max-width: 200px; max-height: 200px; object-fit: cover;">  
  <img src="assets/images/post_pics/An unexpected fractal/6.jpg" alt="Image 17" style="width: 100%; max-width: 200px; max-height: 200px; object-fit: cover;">  
  <img src="assets/images/post_pics/An unexpected fractal/7.jpg" alt="Image 18" style="width: 100%; max-width: 200px; max-height: 200px; object-fit: cover;">  
  <img src="assets/images/post_pics/An unexpected fractal/8.jpg" alt="Image 19" style="width: 100%; max-width: 200px; max-height: 200px; object-fit: cover;">  
  <img src="assets/images/post_pics/An unexpected fractal/9.jpg" alt="Image 20" style="width: 100%; max-width: 200px; max-height: 200px; object-fit: cover;">  
</div>

So I tried to rewrite it in a more efficient fashion, but somewhere on the process I made a mistake in the code, and there it was: an unexpected fractal suddenly appeared.

