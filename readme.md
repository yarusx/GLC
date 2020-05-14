<p>Hello everyone.</p>
I was interested in a dataset called <b>The Global Landslide Catalog Export</b> from <b>NASA</b> site. I like NASA as an organization - their goals and what they are doing. Also, they have a very well structured web page for datasets. This subject isn't relevant to me professionally, but I think it's a good chance to broadening my horizons.
<p>
You could look at the dataset here: <a href="https://data.nasa.gov/Earth-Science/Global-Landslide-Catalog-Export/dd9e-wu2v">NASA</a></p>
<p>Here comes a <i>short description</i> of the GLC dataset: "<b>The Global Landslide Catalog (GLC)</b> was developed with the goal of identifying rainfall-triggered landslide events around the world, regardless of size, impacts or location. The GLC considers all types of mass movements triggered by rainfall, which have been reported in the media, disaster databases, scientific reports, or other sources. The GLC has been compiled since 2007 at NASA Goddard Space Flight Center. This is a unique data set with the ID tag “GLC” in the landslide editor."</p>
<p><i>What kind of analysis could be done with this data?</i></p>
<p>This project consists of such <b>steps (parts)</b>:</p>
<p>1) <b>DB parsing</b> and getting info about the date and place of a Landslide. This could be done with a help of: <p>
- <b><i>builder_big.py</i></b> - interacts directly with NASA web page and creates <b><i>db_big.sqlite</i></b>, or </p>
<p>- <b><i>builder_offline.py</i></b> - does the same job, but with a downloaded <b><i>rows.json</i></b> data file.</p>
<p>Also there is a <b><i>builder_light.py</i></b> that produces a little bit different DB with a smaller quantity of Landslides. Also the source has another JSON structure and another approach for its' parsing. Application produces db.sqlite, which is currently not used on the further stages of project.</p>
<<<<<<< HEAD
2) Two ways of the data <b>analysis and visualization</b>:
<p>- the first one is made with a help of Google Maps (based on Dr. Chuck's files). <b><i>Geo.py</i></b> script writes <b><i>map.js</i><b> file which is used by <a href="https://yarusx.github.io/GLC/map.html"><b><i>map.html</i></b></a>. <b><i>Geo.py</i></b> provides a filtering of Landslides events by the chosen year. Also it provides a small cleaning of the sqlite DB (removing nasty symbols that ruins JS file usage). <b><i>Map.html</i></b> file should be executed for visualization of Landslides on Google Map.</p>
<p>- the second one is made with a help of Google Charts (also based on Dr. Chuck's files). <b><i>lchart.py</i></b> writes <b><i>lchart.js</i><b> file which is used by <a href="https://yarusx.github.io/GLC/lchart.htm"><b><i>lchart.htm</i></b></a>. <b><i>Lchart.py</i></b> also counts top 10 countries by fatal cases caused by Landslides. <b><i>Lchart.htm</i></b> file should be executed for visualization of Landslides on Google Charts.</p></p>
=======
2) <b>Data analysis and visualization</b>:
<p>- with a help of the Google Maps (based on Dr. Chuck's files). <b><i>Geo.py</i></b> script writes a map.js file that is used by <a href="https://yarusx.github.io/GLC/map.html"><b><i>map.html</i></b></a>. <b><i>Geo.py</i></b> provides a filtering of Landslides events by the chosen year. Also it provides a small cleaning of the sqlite DB (removing nasty symbols that ruins JS file usage). <b><i>Map.html</i></b> file should be executed for visualization of Landslides on the Google Map.</p>
<p>- the second way of data analysis and visualization will be a Line Chart. It's still in progress. I plan to finish it until 15.05.2020.</p>
>>>>>>> 631dd88f5fd578fce79dd64cb81625f4403320e1

<i>As a requirement for GLC DB usage I place as a cite these two sources</i>:
Kirschbaum, D. B., Adler, R., Hong, Y., Hill, S., & Lerner-Lam, A. (2010). A global landslide catalog for hazard applications: method, results, and limitations. Natural Hazards, 52(3), 561–575. doi:10.1007/s11069-009-9401-4. [1]
Kirschbaum, D.B., T. Stanley, Y. Zhou (In press, 2015). Spatial and Temporal Analysis of a Global Landslide Catalog. Geomorphology. doi:10.1016/j.geomorph.2015.03.016. [2]

Also big thanks for the support to Dr. Chuck (Charles Severance, <a href="https://twitter.com/drchuck">@drchuck</a>) and his educational materials from Python for Everybody specialization on Coursera.
