#' @title Create a loon object handle
#' 
#' @description This function can be used to create the loon object handles from
#'   a vector of the widget path name and the object ids (in the order of the 
#'   parent-child relationships).
#'   
#'   
#' @details loon's plot handles are useful to query and modify plot states 
#'   via the command line.
#'   
#' @templateVar page learn_R_intro
#' @templateVar section re-creating-object-handles
#' @template see_l_help
#' 
#' @param target loon object specification (e.g. \code{".l0.plot"})
#'   
#' @export
#' 
#' @examples 
#' 
#' # plot handle
#' p <- l_plot(x=1:3, y=1:3)
#' p_new <- l_create_handle(unclass(p))
#' p_new['showScales']
#' 
#' # glyph handle
#' gl <- l_glyph_add_text(p, text=LETTERS[1:3])
#' gl_new <- l_create_handle(c(as.vector(p), as.vector(gl)))
#' gl_new['text']
#' 
#' # layer handle
#' l <- l_layer_rectangle(p, x=c(1,3), y=c(1,3), color='yellow', index='end')
#' l_new <- l_create_handle(c(as.vector(p), as.vector(l)))
#' l_new['color']
#' 
#' # navigator handle
#' g <- l_graph(linegraph(completegraph(LETTERS[1:3])))
#' nav <- l_navigator_add(g)
#' nav_new <- l_create_handle(c(as.vector(g), as.vector(nav)))
#' nav_new['from']
#' 
#' # context handle
#' con <- l_context_add_context2d(nav)
#' con_new <- l_create_handle(c(as.vector(g), as.vector(nav), as.vector(con)))
#' con_new['separator']
from .loon_class import loon, loon_l_plot, loon_l_hist,loon_l_serialaxes,loon_l_graph
from .l_isLoonWidget import l_isLoonWidget
from .tk import tk
from sys import exit
def l_create_handle(target):
    #### target can only support for a single string right now
    if(isinstance(target,loon)):
        loon_obj = target 
        hasRecognized = True
    elif(isinstance(target, str)):
        widget = target 
        if(not l_isLoonWidget(widget)):        
            exit(widget + ' is not a valid loon widget')
        cl = tk.tk.call('info','object','class',widget)
        if(cl == '"::loon::classes::Scatterplot_Widget"'):
            loon_obj = loon_l_plot(widget)
        elif(cl == "::loon::classes::Histogram_Widget"):
            loon_obj = loon_l_hist(widget)
        elif(cl == "::loon::classes::Serialaxes_Widget"):
            loon_obj = loon_l_serialaxes(widget)
        elif(cl ==  "::loon::classes::Graph_Widget"):
            loon_obj = loon_l_graph(widget)
        else:
            loon_obj = loon(widget)
    elif(isinstance(target,list)):
       #### not finish yet 
       exit('not support for the list of targets yet')
    else:
        exit('invalid target.')
    return loon_obj