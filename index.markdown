---
layout: page
#permalink: /term
#my-image: images/term.jpg
---

<!-- Main -->

<div class="container">
	<span class="image main"><img src="images/term.jpg" alt="" /></span>
</div>





<div>
	<div ><p>{{ site.description }}</p>
	<section class="tiles">
		<div class="box alt">
			<div class="row gtr-uniform">
			{% for post in site.posts limit:6%}
			<div class="col-4"><span class="image fit"><a href="{{ post.url }}"><img src="{{ site.url }}/{{ post.small_img }}" alt="" /></a></span>
			<a href="{{ post.url }}">{{ post.title }}</a></div>
			{% endfor %}
		</div></div>
	</section>
	</div>
</div>
