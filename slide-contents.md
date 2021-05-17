<!--
This file defines the contents of each slide.
The reveal.js configuration can be found in index.html
-->

<!-- .slide: class="slide-title" data-background-color="#000000" data-background-image="assets/background.svg" data-background-repeat="no-repeat" data-background-position="center" -->

<div class="talk-title">

# Fatiando a Terra

## open-source tools for geophysics

</div>

<img src="assets/fatiando-logo.svg" style="width: 8%;">

<div class="talk-authors">

### Leonardo Uieda, Santiago Soler, Agustina Pesce

Geophysical Society of Houston <span style="margin: 0 20px">|</span> 20 May 2021

</div>

<img src="assets/university-of-liverpool-white.png" class="title-logo">
<!-- Replace with CONICET and San Juan logos -->
<img src="assets/university-of-liverpool-white.png" class="title-logo">
<img src="assets/university-of-liverpool-white.png" class="title-logo">

<i class="fab fa-twitter fa-fw"></i> [@fatiandoaterra](https://twitter.com/fatiandoaterra)
<span style="margin: 0 20px">|</span>
<i class="fa fa-camera"></i>
Feel free to screenshot/share/reuse/remix this presentation
<span style="margin: 0 20px">|</span>
[<i class="fab fa-creative-commons"></i><i class="fab fa-creative-commons-by"></i> CC-BY 4.0 License](https://creativecommons.org/licenses/by/4.0/)

---

<!-- .slide: class="slide-transition" data-background-color="#222222" -->

<div class="centered">
<div>

# A bit of history

<img src="assets/logo-evolution.svg" style="margin-top: 5%;">

</div>
</div>

---

<!-- .slide: data-background-video="assets/brasil-sao-paulo-rio.mp4" data-background-size="contain" data-background-color="#000000" -->

<div class="r-stretch bottom-right">

Our journey starts in Southeastern Brazil, specifically in São Paulo and Rio de
Janeiro

</div>

---

<!-- .slide: data-background-image="assets/fatiando-as-a-gravmag-gui.svg" data-background-size="contain" data-background-repeat="no-repeat" data-background-color="#000000" -->

<div class="centered">
<div class="quote">

Started around 2008 as a GUI for **2D modelling** developed with
fellow **undergrads** at USP, Brazil

</div>
</div>

---

<!-- .slide: data-background-image="assets/fatiando-as-a-gravmag-gui.svg" data-background-size="contain" data-background-repeat="no-repeat" data-background-color="#000000" -->

<div class="r-stretch bottom-right bottom-dark">

Actual diagram of the GUI workflow retrieved from our version control system.

</div>

---

<!-- .slide: data-background-image="assets/fatiando-first-commit.svg" data-background-size="contain" data-background-repeat="no-repeat" data-background-color="#000000" -->

<div class="r-stretch bottom-right">

Transitioned into the *fatiando* **Python library** in 2010 when I started my
MSc in Rio
(commit: [928515b](https://github.com/fatiando/fatiando/commit/928515b0fcfdccecbc4f661ed2469390ef43ec1d))

</div>

---

<!-- .slide: data-background-image="assets/fatiando-first-commit-vcs.svg" data-background-size="contain" data-background-repeat="no-repeat" data-background-color="#000000" -->

<div class="r-stretch bottom-right">

**Learned a lot** about software development: tests, packaging, documentation,
<br>
version control (went through SVN, Mercurial, and Git), and more.

</div>

---

<!-- .slide: data-background-image="assets/fatiando-first-gallery.jpg" data-background-size="contain" data-background-repeat="no-repeat" data-background-color="#000000" -->

<div class="r-stretch bottom-left bottom-dark">

Around 2011 we built the first website and gallery. We ended up building a 2D
GUI and much more,
<br>
from seismic to potential fields and heat flow.

</div>

---

<!-- .slide: data-background-image="assets/fatiando-docs-v0.1.jpg" data-background-size="contain" data-background-repeat="no-repeat" data-background-color="#000000" -->

<div class="r-stretch bottom-left bottom-dark">

First documentation built using [sphinx](https://www.sphinx-doc.org) for
**v0.1** (2013). doi:[10.5281/zenodo.16207](https://doi.org/10.5281/zenodo.16207)

</div>

---

<!-- .slide: data-background-image="assets/fatiando-docs-v0.2.jpg" data-background-size="contain" data-background-repeat="no-repeat" data-background-color="#000000" -->

<div class="r-stretch bottom-left bottom-dark">

Updated documentation for **v0.2** (2014). doi:[10.6084/m9.figshare.1115194](https://doi.org/10.6084/m9.figshare.1115194)

</div>

---

<!-- .slide: data-background-image="assets/fatiando-docs-v0.5.jpg" data-background-size="contain" data-background-repeat="no-repeat" data-background-color="#000000" -->

<div class="r-stretch bottom-left bottom-dark">

Last update for **v0.5** (2016). doi:[10.5281/zenodo.157746](https://doi.org/10.5281/zenodo.157746)

</div>

---

<div class="container">
<div class="col-left" style="padding-right: 5%">

# <i class="far fa-thumbs-up" style="margin-right: 20px;"></i> The good parts

<hr>

<ul class="fa-ul">

<li>
<span class="fa-li"> <i class="fa fa-lightbulb fa-fw"></i> </span>
State-of-the-art algorithms
</li>

<li>
<span class="fa-li"> <i class="fa fa-file-alt fa-fw"></i> </span>
Used in several thesis & papers (>70 citations)
</li>

<li>
<span class="fa-li"> <i class="fa fa-users fa-fw"></i> </span>
3-4 active contributors
</li>

<li>
<span class="fa-li"> <i class="fa fa-chalkboard-teacher fa-fw"></i> </span>
Teaching through simulation
</li>

</ul>

</div>
<div class="col-right fragment" style="padding-left: 5%">

# <i class="far fa-thumbs-down" style="margin-right: 20px;"></i> The bad parts

<hr>

<ul class="fa-ul">

<li>
<span class="fa-li"> <i class="fa fa-gamepad fa-fw"></i> </span>
Too many toy problems and experimental code
</li>

<li>
<span class="fa-li"> <i class="fas fa-vial fa-fw"></i> </span>
Not designed for testability
</li>

<li>
<span class="fa-li"> <i class="fa fa-tools fa-fw"></i> </span>
Difficult to maintain
</li>

<li>
<span class="fa-li"> <i class="fa fa-landmark fa-fw"></i> </span>
Unstable foundations for growth
</li>

</ul>
</div>

---

New tools

---

<!-- .slide: class="slide-transition" data-background-color="#000000" data-background-image="assets/demo-time.gif" data-background-repeat="no-repeat" data-background-position="center" data-background-opacity="70%" -->

<div class="centered">
<div>

# Demo time!

</div>
</div>

---

<!-- .slide: class="slide-transition" data-background-color="#222222" -->

<div class="centered">
<div>

# Fatiando is not just code,<br> it's a **community**

</div>
</div>

---

<!-- .slide: class="slide-license" -->

<div class="centered">
<div>

<p class="license-icons">
<i class="fab fa-creative-commons"></i><i class="fab fa-creative-commons-by"></i>
</p>

Unless otherwise noted,
the contents of this presentation are
licensed under the
<br>
[Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

</div>
</div>
