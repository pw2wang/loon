from .l_layer import l_layer,l_layer_polygons,l_layer_polygon,l_layer_group
from .l_throwErrorIfNotLoonWidget import l_throwErrorIfNotLoonWidget
from .retrieve_name import retrieve_name
from .l_plot import l_plot
from .l_scaleto import l_scaleto_world
import geopandas
import shapely
from matplotlib.colors import is_color_like
from sys import exit 
#' @title Create a plot with a map layer
#'
#' @description Creates a scatterplot widget and layers the map in front.
#'
#' @param x object of class map (defined in the maps library)
#' @param ... arguments forwarded to \code{\link{l_layer.map}}
#'
#' @return Scatterplot widget plot handle
#'
#' @export
#' @export l_plot.map
#'
#' @seealso \code{\link{l_layer}}, \code{\link{l_layer.map}},
#'   \code{\link[maps]{map}}
#'
#' @examples
#' if (requireNamespace("maps", quietly = TRUE)) {
#'    p <- l_plot(maps::map('world', fill=TRUE, plot=FALSE))
#' }


def l_plot_map(x, **options):
    p = l_plot()
    l_layer_map(p, x, label="Map",  **options)
    l_scaleto_world(p)
    return p

#' @title Add a Map of class map as Drawings to Loon plot
#'
#' @description The maps library provides some map data in polygon which can be
#'   added as drawings (currently with polygons) to Loon plots. This function
#'   adds map objects with class map from the maps library as background
#'   drawings.
#'
#' @template param_widget
#' @param x a map object of class \code{\link[maps]{map}} as defined in the
#'   \code{maps} \R package
#' @inheritParams l_layer_polygon
#' @template param_parent
#' @template param_index
#' @param asSingleLayer if \code{TRUE} then all the polygons get placed in a
#'   n-dimension layer of type polygons. Otherwise, if \code{FALSE}, each
#'   polygon gets its own layer.
#' @template param_dots_method_not_used
#'
#' @return If \code{asSingleLayer=TRUE} then returns layer id of polygons layer,
#'   otherwise group layer that contains polygon children layers.
#'
#' @export
#' @export l_layer.map
#'
#' @examples
#' if (requireNamespace("maps", quietly = TRUE)) {
#'   canada <- maps::map("world",  "Canada",
#'                       fill=TRUE, plot=FALSE)
#'   p <- l_plot()
#'   l_map <- l_layer(p, canada,
#'                    asSingleLayer=TRUE, color = "cornsilk")
#'   l_map['color'] <- ifelse(grepl("lake", canada$names, TRUE),
#'                            "lightblue", "cornsilk")
#'   l_scaleto_layer(p, l_map)
#'   l_map['active'] <- FALSE
#'   l_map['active'] <- TRUE
#'   l_map['tag']
#' }
def l_layer_map(widget, x, color="cornsilk", linecolor="black", linewidth=1,
                    label= None, parent="root", index=0, asSingleLayer=True, **options):

    l_throwErrorIfNotLoonWidget(widget)
    map = x

    if(not isinstance(map,geopandas.GeoDataFrame)):
        exit("map is not a map object from the geopandas package.")
    if(label == None):
        label = retrieve_name(map)

    if(isinstance(color,str) and not is_color_like(color)):
        exit("color needs to be a color or \"\"")
    elif(isinstance(color,(list,tuple))):
        check = [not is_color_like(temp) for temp in color]
        if(sum(check) > 0):
            exit("color needs to be a color or \"\"")

    if(isinstance(linecolor,str) and not is_color_like(linecolor)):
        exit("linecolor needs to be a color or \"\"")
    elif(isinstance(linecolor,(list,tuple))):
        check = [not is_color_like(temp) for temp in linecolor]
        if(sum(check) > 0):
            exit("linecolor needs to be a color or \"\"")


    if(isinstance(linewidth,int)):
        if(linewidth < 0):
            exit("linewidth needs to be numeric and >=0")
    elif(isinstance(linewidth,(tuple,list))):
        check = [temp < 0 for temp in linewidth]
        if(sum(check) > 0):
            exit("linewidth needs to be numeric and >=0")


    npolygons = sum([len(x) if isinstance(x,shapely.geometry.multipolygon.MultiPolygon) else 1 for x in map.geometry])

    res = None

    if (npolygons == 1):
        print(111)
        res = l_layer_polygon(widget, x=list(map.boundary[0].xy[0]), y=list(map.boundary[0].xy[1]),
                               color=color,
                               linecolor=linecolor,
                               linewidth=linewidth,
                               label=label)
    else:
        if(isinstance(color,str)):
            color = [color]*npolygons
        elif(isinstance(color,(list,tuple))):
            if(len(color) != 1 and len(color) != npolygons):
                print("only first color element used as length not equal to number of polygons")
                color = [color[0]]*npolygons


        if(isinstance(linecolor,str)):
            linecolor = [linecolor]*npolygons
        elif(isinstance(linecolor,(list,tuple))):
            if(len(linecolor) != 1 and len(linecolor) != npolygons):
                print("only first linecolor element used as length not equal to number of polygons")
                linecolor = [linecolor[0]]*npolygons


        if(isinstance(linewidth,(int,float))):
            linewidth = [linewidth]*npolygons
        elif(isinstance(linewidth,(list,tuple))):
            if(len(linewidth) != 1 and len(linewidth) != npolygons):
                print("only first linewidth element used as length not equal to number of polygons")
                linewidth = [linewidth[0]]*npolygons    

            
        #newPos <- c(0, pos, length(map$x)+1)
        #ids <- rep(NA, npolygons)
        if(asSingleLayer):
            xlist = []
            ylist = []
            tag = []
            # for i in range(npolygons):
            #     print('------------ '+ str(i))
            #     obj = map.geometry[i]
            #     if(isinstance(obj,shapely.geometry.polygon.Polygon)):
            #         xlist.append(list(obj.boundary.xy[0]))
            #         ylist.append(list(obj.boundary.xy[1]))
            #         tag.append(map.name[i])
            #     elif(isinstance(obj,shapely.geometry.multipolygon.MultiPolygon)):
            #         for j in obj:
            #             xlist.append(list(j.boundary.xy[0]))
            #             ylist.append(list(j.boundary.xy[1]))
            #             tag.append(map.name[i])
            #     else:
            #         exit('not support for ', type(obj))
            for i,j in zip(map.geometry,map.name):
                print('------------ '+ j)
                if(isinstance(i,shapely.geometry.polygon.Polygon)):
                    xlist.append(list(i.boundary.xy[0]))
                    ylist.append(list(i.boundary.xy[1]))
                    tag.append(j)
                elif(isinstance(i,shapely.geometry.multipolygon.MultiPolygon)):
                    for k in i:
                        xlist.append(list(k.boundary.xy[0]))
                        ylist.append(list(k.boundary.xy[1]))
                        tag.append(j)
                else:
                    exit('not support for ', type(i))

            res = l_layer_polygons(widget, xlist, ylist,
                        color=color,
                        linecolor=linecolor,
                        linewidth=linewidth,
                        tag=tag,
                        label=label,
                        parent=parent,
                        index='end')
        else:
            print('----not done yet')
            res = l_layer_group(widget, label=label, parent=parent, index=index)
            
    return res 