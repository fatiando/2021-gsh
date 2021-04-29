# Fatiando a Terra: Open-source tools for geophysics

Online talk given to the Geophysical Society of Houston (GSH) in 2021
to introduce the project, in particular Boule and Harmonica.

| | Info |
|--:|:------|
| When | 22 May 2021 XX:XX UTC |
| Slides | Add a link to the slides |
| Recording | Will this be recorded? |

## Notes and TODO

* Available time: 40 mins (double check)

## Abstract

The Fatiando a Terra project (https://www.fatiando.org) is a collection of open-source Python libraries for geophysics which cover a range of functionalities, from data download and processing to modeling and inversion. 
In this opportunity we will present the two libraries that are focused on potential fields: Harmonica and Boule. 
Boule implements reference ellipsoids (including oblate ellipsoids, spheres, and soon triaxial ellipsoids), conversions between ellipsoidal and geocentric spherical coordinates, and normal gravity calculations.
The latter are performed using analytical expressions for gravity fields at any point outside of the ellipsoid. 
Harmonica provides tools for processing, forward modelling, and inversion of gravity and magnetic data. 
We will demonstrate its use to compute Bouguer gravity disturbances by forward modelling the topography with prisms, removing a 2nd order regional trend, and interpolating it onto a regular grid at a constant height using the equivalent layer technique.
Both libraries are still evolving as we continue to refine their goals and scopes.
We invite everyone to get involved in the development, whether it's through coding, writing documentation, or giving feedback.

## Speakers

* Leonardo Uieda 
    * Department of Earth, Ocean and Ecological Sciences, School of Environmental Sciences, University of Liverpool, UK
    * https://www.leouieda.com
* Santiago Soler
    * Instituto Geofísico Sismológico Volponi, Universidad Nacional de San Juan, Argentina
    * CONICET, Argentina
    * https://santisoler.github.io
* Agustina Pesce
    * Instituto Geofísico Sismológico Volponi, Universidad Nacional de San Juan, Argentina
    * CONICET, Argentina
    * https://aguspesce.github.io

## Resources

Find out more:

* Harmonica documentation: https://www.fatiando.org/harmonica
* Boule documentation: https://www.fatiando.org/boule
* Tutorial for Boule and Harmonica at Transform 2021: https://youtu.be/0bxZcCAr6bw and https://github.com/fatiando/transform21
* Presentation at EGU2021: https://doi.org/10.5194/egusphere-egu21-8291 and https://github.com/fatiando/egu2021

Get involved in the project:

* Join our Slack chatroom: http://contact.fatiando.org
* Come to an open community call: https://www.youtube.com/playlist?list=PLPA_RM8wsOqIEBLICo3v7f_A1WnLcwJld
* Follow Fatiando a Terra on Twitter: https://twitter.com/fatiandoaterra

## Bios

### Agustina Pesce

<img src="https://raw.githubusercontent.com/aguspesce/aguspesce.github.io/master/imgs/about.jpg"
    style="height: 300px">

PhD in Geophysics focused in applied geophysics, processing and analyzing gravity and magnetic data. Now she is studying the subduction zones through geodynamical numerical modeling.

### Santiago Soler

<img src="https://santisoler.github.io/images/about.jpg"
    style="height: 300px">

Physicist and PhD Student in Geophysics. His research is focused on new methodologies for forward and inverse modelling potential field data. He is one of the core developers of Fatiando a Terra, leading the development of the Harmonica library for processing and modelling gravity and magentic data.

### Leonardo Uieda

<img src="https://www.leouieda.com/images/profile/ness.jpg"
    style="height: 300px">

Geophysicist specializing in the development of methods for determining the inner structure of the Earth from geophysical observations, mainly disturbances in the Earth's gravity and magnetic fields. Developer of open-source software for processing, modeling, and visualizing geophysical data. Advocate for openness in the scientific process and the adoption of best practices in computational research.

## Logo

<img src="https://raw.githubusercontent.com/fatiando/logo/master/fatiando-logo-background.png" 
    style="height: 300px">

## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img
alt="Creative Commons License" style="border-width:0"
src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br>
This content is licensed under a <a rel="license"
href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution
4.0 International License</a>.
