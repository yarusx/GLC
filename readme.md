<p>Hello everyone.</p>
I was interested in a dataset called Global Landslide Catalog Export from NASA site. I like NASA as an organization: their goals and what they are doing. Also, they have a very well structured web page for datasets. This subject isn't relevant to me professionally, but I think it will be interesting to work on this project just for spreading my worldwide.
The database could be downloaded from here: https://dev.socrata.com/foundry/data.nasa.gov/dd9e-wu2v
You need to push "Export dataset as CSV ".
Also, you could look at the dataset here: https://data.nasa.gov/Earth-Science/Global-Landslide-Catalog-Export/dd9e-wu2v
Here is a short description of the GLC dataset: "The Global Landslide Catalog (GLC) was developed with the goal of identifying rainfall-triggered landslide events around the world, regardless of size, impacts or location. The GLC considers all types of mass movements triggered by rainfall, which have been reported in the media, disaster databases, scientific reports, or other sources. The GLC has been compiled since 2007 at NASA Goddard Space Flight Center. This is a unique data set with the ID tag “GLC” in the landslide editor."
What kind of analysis could be done with this data?
I thought that it would be great to parse the DB and get the info about the date and place of the disaster. Then compile that into SQlite DB. And after that visualize it through the Google API on the Google map (based on Dr. Chuck's application). The script that produces files for visualization should have a request for the year of disaster (it would be a way of filtering).
As a requirement for GLC DB usage I place as a cite these two sources :
Kirschbaum, D. B., Adler, R., Hong, Y., Hill, S., & Lerner-Lam, A. (2010). A global landslide catalog for hazard applications: method, results, and limitations. Natural Hazards, 52(3), 561–575. doi:10.1007/s11069-009-9401-4. [1]
Kirschbaum, D.B., T. Stanley, Y. Zhou (In press, 2015). Spatial and Temporal Analysis of a Global Landslide Catalog. Geomorphology. doi:10.1016/j.geomorph.2015.03.016. [2]

Also big thanks for the support to Dr. Chuck (Charles Severance, <a href="https://twitter.com/drchuck">@drchuck</a>) and his educational materials from Python for Everybody specialization on Coursera.
