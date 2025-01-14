.. currentmodule:: diver

.. ipython:: python
   :suppress:

   from diver import *
   import matplotlib
   %gui tk

Introduction 
===============


    | "Exposure, the effective laying open of the data to display the unanticipated, 
    | is to us a major portion of data analysis."  ... John Tukey and Martin Wilk (1966) 

Because loon is an interactive visualization system, this introduction is meant as a "hands on" tutorial.
Not all interactions are from the command line (programmatic).
Suggestions for interactions will also be given and questions that draw attention to the outcome of interactions.

After completing the tutorial, there are numerous other examples of using loon which can be explored.  These include

- many of the common arguments to `l_plot()` are described in the help topic `l_plot_arguments`
- help(<func_name>) can be used to get the detials for the query function, or alternatively online via as `l_web()`
- the loon website appearing from `l_help()` or `l_web()`.

Here, we will walk through some of the **basic** functionality.


--- 

`l_plot()` the basic `loon` plot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Begin with a simple scatterplot of the `quakes` data from `R`

.. ipython:: python

    l_plot(x = quakes["long"], 
        y = quakes["lat"], 
        xlabel = "longitude", 
        ylabel = "latitude",
        title = "Tonga trench earthquakes");


This prints the above information on the loon plot (more on this later) and causes 
two windows to appear.  

One is the scatterplot:

.. image:: ./images/intro/quakesOriginal.png
    :width: 400px
    :align: center

and the other a "loon inspector":

.. image:: ./images/intro/inspectorQuakesOriginal.png
    :width: 250px
    :align: center

For the moment we'll focus mainly on the scatterplot.

--- 



Direct manipulation on the plot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The loon scatterplot is highly interactive and can be **directly manipulated** using the mouse. 
Several interactions are immediately available.

In what follows, images of a two button mouse (left is primary, right secondary) with a scroll wheel will be used to indicate the interaction.
The colour red indicates selection, arrows and double images suggest movement, and any modifier keys are shown in the body of the mouse.

---

Panning
^^^^^^^

To pan the plot, select the plot interior with the right (or secondary) mouse button and move the mouse (with the button still down).  The direction of panning can be constrained by holding down the named modifier keys while panning. 
.. image:: ./images/intro/panning.png
    :width: 300px
    :align: center

Try it. Select anywhere on the scatterplot and move it

- freely about
- only horizontally
- only vertically

**Question**:  How did the inspector change in response to each movement?

Reproduce these movements on the smaller "World View" plot appearing at the top of the inspector.  

How does the larger scatterplot change?

---

Zooming
^^^^^^^

Another way to dynamically focus on different parts of the plot is by zooming, using **scrolling**:

.. image:: ./images/intro/zooming.png
    :width: 300px
    :align: center

To try it, note that there is a small cluster of 16 points towards the top left of the scatterplot. 

On the scatterplot,

- zoom in and out and move the plot around until **only** these 16 points appear in the scatterplot

- use the restricted horizontal and vertical zooming so that the same 16 points occupy as much of the scatterplot's space as possible

**Question**: How has the inspector changed in response?

On the inspector click on the button titled `plot`.  What happened?

Using zooming and panning on the "World View" 

- focus the scatterplot on the **same** 16 points.

--- 

Selecting
^^^^^^^^^

There are two ways to directly select points on the scatterplot using the mouse: either by selection (one at a time or multiple selections) or by "sweep selection" as shown below:

.. image:: ./images/intro/selecting.png
    :width: 300px
    :align: center

To try this out, on the scatterplot (which should contain only 16 points)

- place the mouse over the topmost point and click the left (or primary) mouse button
    - the point will be highlighted (magenta coloured)

- hold the shift key down and select the leftmost, rightmost and bottom most points of the 16
    - there should now be 4 magenta points 

- colour these 4 points light blue and change their glyph to a triangle 
    - click on the background of the plot to see the change in colour

**Question**: How has the inspector changed?

Now try a holding the left mouse button down and move the mouse.  

This is called **sweeping** or **sweep selection** and allows us to sweep out a contiguous area of the plot.

- use sweep select to identify, and give different colours (none black) to 4 different (roughly) contiguous groups of your choice from the 16 points.

**Check**: The 16 points should now be separated by colour into 4 groups and by glyph shape into 2 groups.

**Question**: How has the inspector changed? 

You will have already discovered how to colour selected points from the inspector.  You can now use the inspector to **select** points by colour:

- **from the inspector**, select all the points of each colour in turn.

--- 

The inspector -- interacting with the plot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By the above experimentation, you will have already discovered how the inspector is used to change the loon plot. 

For example, try checking the "guides" box on the inspector to place a background grid of guide lines on the loon plot.  Unchecking removes the guide lines.

The loon inspector consists of several component pieces.

At the top is the "World View" which shows a miniature version of the **whole** of the current plot, what is displayed there, and what is active.

Below the "World View"  are a few tabs.  The default (and most used) one is the "Analysis" tab where common interactions are separated into three regions: the "Plot", the "Select", and the "Modify" systems.

Try (in order) the following interactions between the inspector and the plot:

1. select the black points only  
2. scale the plot to the selected points 
3. invert the selection 
4. colour the selected points red 
5. select all points, and make them all have open circles as glyphs 
6. select the red points and deactivate them 
7. select brushing mode 
8. brush select the remaining black points dividing them into two groups 
9. colour one of these groups blue, the other orange 
10. turn off the brush 
11. re-activate the points 
12. scale the scatterplot to the "world" 
13. add guides (**no** scales) 


**Check**: You should have a scatterplot of open circles with three clusters of points in red, blue, and orange

--- 

More on direct manipulation  
~~~~~~~~~~~~~~~~~~~~~~~~~~~

on brushing
^^^^^^^^^^^

You should have a scatterplot of open circles with three clusters of points in red, blue, and orange.

Use the functionality of the loon inspector to (in order)

1. Using only colour selection from the inspector, select the largest group (and no others) 
2. Turn on brushing (as opposed to sweeping) mode 
3. Under **dynamic** selection, choose **deselect** 
4. Over the scatterplot use this brush mode to **deselect** the region nearest the highest density (shaped a bit like a question mark  -- ?) 
5. Colour the selected points  green (i.e. low density region of largest coloured group) 

You should now have four different coloured groups or clusters. 

**For fun**, in the inspector

1. select the green group
2. under **dynamic** selection, choose  **invert**
3. move the brush over the scatterplot
4. move the brush over the scatterplot while holding the `<Shift>` key

**Question**: What is going on?  When might this functionality be useful? 

--- 

on selection
^^^^^^^^^^^^

When done, turn the selection back to the defaults:

.. image:: ./images/intro/inspectorSelectDefaults.png
    :width: 300px
    :align: center

That is,

- [static:] none
- [dynamic:]  select
- [by:] sweeping


Shift selection works with any mix of

- individual point selection
- static selection
- dynamic selection by sweeping or brushing
- by color

**Exercise**: Try out different combinations of the above selections.


--- 

moving points
^^^^^^^^^^^^^

For a variety of reasons, we sometimes want to (temporarily) move points in a scatterplot.


From the inspector:

1. deactivate all but the small red group 
2. select the red group and scale the plot to the selected 
3. with these selected points, explore the effect of each of the `move` modifications on the configuration of the selected points 
4. describe in words what each one does


From the scatterplot, selected points may be moved by hand 

- one at a time using `<Ctrl>-<Left-button>`
- in groups using `<Shift><Ctrl><Left-button>`

For example:

1. select the red group
2. move the red group to the bottom of the plot
3. return the red group to its original location

--- 

adding colours to the inspector
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: ./images/intro/inspectorQuakesPlus10Cols.png
    :width: 300px
    :align: center


More colours can be added directly by clicking on the `+` or the `+5` in the colour modification section of the inspector.

- clicking `+5` twice adds 10 new colours
- these colours will persist with the inspector for every loon scatterplot
the inspector palette of colours

The loon system **default** list of colours get be found programmatically:

.. ipython:: python

    l_getColorList();


Note:

- loon colours are 6 hexadecimal digits in length and can be a named colour(e.g red, blue)
- being constrained to tcl/tk colours, no alpha level is available at this time in loon

--- 

changing the inspector palette of colours
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At the **beginning of a loon session** (that is, immediately after executing `import loon`) you might choose to change the default palette for the inspector to something that suits your tastes/problem.

**Note**: There may be unintended side effects to changing the inspector colours after a plot (and hence the inspector) has been created so this should be avoided.

A variety of functions exist to change an inspector's palette of colours:

.. ipython:: python

    l_setColorList_baseR()                             
    # base R palette
    l_setColorList_ColorBrewer("Set2")                 
    # colorblind friendly choice from ColorBrewer
    l_setColorList_hcl(luminance = 80)                 
    # set of hcl colours
    l_setColorList_ggplot2()                           
    # ggplot2's palette 
    l_setColorList_loon()                              
    # default loon palette;

To change the palette

- execute one of these functions 
- if the inspector is open (not recommended), then select the inspector and
close it to force a refresh its colour palette.


`l_setColorList_loon()` returns the inspector to the default loon colour palette.


--- 

Programmatic manipulation 
~~~~~~~~~~~~~~~~~~~~~~~~~~~

accessing the plot
^^^^^^^^^^^^^^^^^^

The plot itself is a (tcl) data structure and can be assigned to an python variable.

Either at construction (the preferable way):

.. ipython:: python

    # loon graphics (note that the result is assigned to p)
    p = l_plot(x = quakes.long, y = quakes.lat, 
                xlabel = "longitude", ylabel = "latitude",
                title = "Tonga trench earthquakes");


or, if (as we did) you forgot to do that or reassigned something else to that variable (more likely), by accessing the plot from its `tcl` string:

.. ipython:: python

    # 4. accessing the plot from its string representation
    p = l_create_handle(".l0.plot");


Note that this string `".l0.plot"` appears on the right side of the window title of an `l_plot`.

Do this and assign your plot to `p`.  You might have to look at the window to get the string if you have created more than one `l_plot()`.


--- 

printing the plot
^^^^^^^^^^^^^^^^^

Were we to now print `p`

.. ipython:: python

    p.plot;

we get the string name of the plot, but with a class attribute.  This is the **value** of `p` and provides us access to a  very rich data structure,  but one whose values reside in `tcl`. 

**Exercise**: Try this.  Change `p` by direct manipulation in `loon` and repeat. 

This allows the visual representation of a `loon` plot to be displayed at any time.  

---

getting plot contents
^^^^^^^^^^^^^^^^^^^^^^

There are `names` associated with a loon plot indicating its contents or **states**:

.. ipython:: python
   
    p.names;


These features of `p` can be directly accessed the `[]` function.

For example, 

.. ipython:: python

    p["showGuides"];

A more meaningful example might be identify groups with the colours of the points.  
This could be done simply as follows 

.. ipython:: python

    cols_saved = ["red", "red", "orange", "red", "red", "orange", 
    "black", "orange", "orange", "red", "red", "black", 
    "red", "red", "black", "orange", "black", "red", 
    "red", "red", "red", "black", "red", "orange", 
    "red", "red", "black", "red", "red", "red", 
    "red", "black", "orange", "red", "orange", "red", 
    "black", "red", "red", "black", "orange", "orange", 
    "red", "orange", "black", "orange", "orange", "black", 
    "red", "orange", "red", "orange", "black", "red", 
    "red", "red", "red", "red", "red", "red", 
    "red", "red", "steelblue", "black", "red", "orange", 
    "red", "red", "red", "orange", "orange", "orange", 
    "black", "red", "red", "red", "orange", "black", 
    "red", "orange", "orange", "red", "red", "orange", 
    "red", "orange", "black", "red", "orange", "orange", 
    "black", "black", "red", "black", "orange", "red", 
    "orange", "red", "black", "red", "orange", "red", 
    "red", "orange", "red", "orange", "orange", "black", 
    "orange", "orange", "orange", "red", "red", "red", 
    "red", "red", "steelblue", "steelblue", "black", "black", 
    "black", "red", "red", "red", "orange", "black", 
    "orange", "red", "orange", "orange", "orange", "red", 
    "black", "red", "red", "black", "orange", "orange", 
    "orange", "orange", "steelblue", "red", "black", "orange", 
    "steelblue", "orange", "orange", "black", "red", "red", 
    "orange", "black", "orange", "black", "black", "red", 
    "black", "red", "black", "black", "red", "red", 
    "black", "orange", "orange", "orange", "orange", "orange", 
    "red", "black", "red", "red", "red", "red", 
    "red", "orange", "red", "orange", "red", "red", 
    "red", "orange", "orange", "red", "red", "orange", 
    "red", "red", "red", "orange", "orange", "black", 
    "red", "red", "orange", "red", "orange", "orange", 
    "red", "red", "red", "red", "red", "orange", 
    "steelblue", "red", "red", "red", "orange", "red", 
    "orange", "red", "orange", "orange", "red", "red", 
    "orange", "red", "orange", "red", "orange", "black", 
    "orange", "red", "red", "black", "orange", "orange", 
    "orange", "black", "red", "red", "red", "orange", 
    "red", "red", "orange", "red", "black", "red", 
    "red", "orange", "black", "red", "orange", "red", 
    "red", "orange", "red", "black", "black", "black", 
    "red", "black", "orange", "red", "orange", "black", 
    "red", "red", "orange", "red", "black", "red", 
    "red", "orange", "black", "black", "red", "red", 
    "red", "red", "red", "red", "red", "red", 
    "red", "red", "red", "red", "orange", "red", 
    "black", "orange", "orange", "red", "red", "orange", 
    "red", "red", "red", "black", "red", "red", 
    "orange", "orange", "red", "red", "orange", "black", 
    "steelblue", "orange", "orange", "red", "steelblue", "red", 
    "red", "red", "red", "orange", "steelblue", "steelblue", 
    "red", "red", "orange", "red", "red", "black", 
    "red", "black", "black", "orange", "red", "orange", 
    "black", "orange", "red", "black", "orange", "black", 
    "orange", "red", "orange", "black", "red", "orange", 
    "orange", "orange", "orange", "orange", "orange", "orange", 
    "orange", "orange", "orange", "orange", "orange", "orange", 
    "orange", "orange", "orange", "black", "red", "orange", 
    "orange", "red", "black", "red", "orange", "black", 
    "red", "orange", "red", "orange", "black", "orange", 
    "red", "red", "red", "orange", "red", "orange", 
    "red", "red", "orange", "orange", "red", "orange", 
    "orange", "orange", "black", "black", "orange", "black", 
    "red", "orange", "red", "orange", "black", "orange", 
    "orange", "orange", "red", "red", "red", "red", 
    "red", "orange", "red", "steelblue", "orange", "black", 
    "orange", "red", "red", "red", "red", "black", 
    "red", "orange", "orange", "orange", "black", "red", 
    "orange", "black", "black", "orange", "orange", "orange", 
    "red", "orange", "orange", "red", "orange", "orange", 
    "red", "red", "black", "red", "red", "red", 
    "red", "red", "orange", "orange", "black", "red", 
    "red", "orange", "black", "orange", "black", "red", 
    "orange", "orange", "orange", "red", "red", "red", 
    "orange", "red", "black", "orange", "orange", "black", 
    "red", "orange", "red", "red", "orange", "red", 
    "red", "red", "orange", "red", "black", "orange", 
    "red", "orange", "orange", "orange", "orange", "black", 
    "orange", "orange", "orange", "orange", "red", "orange", 
    "red", "red", "orange", "orange", "red", "orange", 
    "orange", "red", "red", "steelblue", "orange", "black", 
    "red", "red", "orange", "black", "orange", "orange", 
    "red", "orange", "orange", "orange", "orange", "black", 
    "red", "red", "black", "black", "black", "red", 
    "orange", "orange", "orange", "red", "red", "orange", 
    "black", "orange", "orange", "red", "orange", "red", 
    "orange", "black", "orange", "red", "black", "black", 
    "red", "orange", "black", "black", "orange", "black", 
    "orange", "black", "red", "black", "black", "red", 
    "black", "black", "black", "black", "black", "black", 
    "black", "red", "orange", "red", "red", "black", 
    "black", "orange", "orange", "orange", "orange", "orange", 
    "red", "black", "red", "orange", "orange", "orange", 
    "red", "orange", "orange", "red", "orange", "orange", 
    "black", "orange", "red", "orange", "red", "orange", 
    "red", "red", "red", "orange", "black", "red", 
    "black", "red", "red", "orange", "black", "red", 
    "red", "red", "red", "red", "black", "black", 
    "orange", "black", "black", "red", "orange", "orange", 
    "orange", "orange", "red", "red", "black", "orange", 
    "orange", "orange", "red", "orange", "orange", "black", 
    "black", "red", "orange", "red", "orange", "black", 
    "red", "black", "orange", "orange", "red", "red", 
    "black", "red", "orange", "red", "black", "red", 
    "red", "orange", "orange", "red", "orange", "red", 
    "orange", "black", "orange", "red", "red", "black", 
    "orange", "orange", "red", "orange", "orange", "orange", 
    "orange", "red", "red", "red", "black", "red", 
    "steelblue", "black", "red", "orange", "red", "red", 
    "orange", "red", "red", "red", "red", "red", 
    "red", "red", "red", "orange", "red", "black", 
    "red", "red", "black", "orange", "orange", "red", 
    "red", "red", "black", "orange", "orange", "red", 
    "orange", "black", "red", "red", "red", "red", 
    "red", "red", "red", "red", "red", "red", 
    "red", "orange", "black", "red", "black", "black", 
    "red", "red", "orange", "orange", "red", "orange", 
    "orange", "red", "orange", "black", "orange", "black", 
    "red", "steelblue", "red", "orange", "orange", "red", 
    "black", "red", "red", "red", "black", "black", 
    "red", "red", "red", "red", "red", "orange", 
    "orange", "red", "black", "orange", "orange", "red", 
    "red", "orange", "red", "orange", "orange", "orange", 
    "red", "orange", "orange", "orange", "red", "red", 
    "red", "orange", "red", "black", "red", "black", 
    "orange", "orange", "black", "orange", "orange", "red", 
    "orange", "orange", "black", "black", "orange", "orange", 
    "black", "orange", "orange", "red", "orange", "red", 
    "red", "red", "orange", "red", "black", "red", 
    "black", "black", "orange", "orange", "red", "orange", 
    "black", "red", "orange", "red", "red", "red", 
    "red", "orange", "red", "orange", "black", "red", 
    "orange", "red", "orange", "red", "orange", "steelblue", 
    "red", "orange", "red", "red", "red", "red", 
    "red", "orange", "black", "orange", "red", "red", 
    "orange", "orange", "red", "red", "red", "orange", 
    "red", "red", "black", "red", "black", "orange", 
    "orange", "orange", "orange", "orange", "orange", "red", 
    "red", "orange", "black", "red", "orange", "black", 
    "red", "orange", "orange", "black", "red", "red", 
    "red", "red", "red", "red", "orange", "black", 
    "black", "orange", "red", "orange", "steelblue", "orange", 
    "orange", "black", "red", "red", "red", "red", 
    "black", "black", "red", "orange", "black", "black", 
    "red", "black", "black", "red", "red", "red", 
    "red", "red", "red", "red", "orange", "red", 
    "black", "black", "orange", "red", "black", "black", 
    "orange", "orange", "black", "red", "black", "orange", 
    "red", "red", "orange", "red", "orange", "red", 
    "orange", "orange", "orange", "red", "red", "red", 
    "red", "black", "black", "orange", "red", "black", 
    "orange", "red", "black", "black", "orange", "orange", 
    "orange", "red", "black", "orange", "red", "red", 
    "orange", "red", "black", "orange", "orange", "black", 
    "orange", "red", "red", "orange", "orange", "orange", 
    "red", "orange", "red", "red", "red", "orange", 
    "red", "orange", "orange", "orange", "red", "orange", 
    "orange", "orange", "red", "orange", "orange", "red", 
    "red", "red", "orange", "orange", "red", "orange", 
    "orange", "black", "black", "orange", "orange", "red", 
    "red", "red", "black", "orange", "orange", "orange", 
    "orange", "black", "orange", "orange", "orange", "orange", 
    "red", "black", "red", "black", "orange", "orange", 
    "orange", "black", "black", "black", "red", "red", 
    "red", "red", "orange", "red", "orange", "red", 
    "black", "orange", "orange", "black"
    ]
    p["color"] = cols_saved;


.. ipython:: python
    import numpy as np
    unique_cols = np.unique(p['color'])
    group1 = p['color'] == unique_cols[0]

    # 5. Number in group 1 (e.g. as you might have -- here from saved colours)
    sum(group1)

    # 6. Data on first few quakes in group 1.
    quakes.loc[group1,].head();



Alternatively, a function could be written to save the groups as a list of logical vectors (one for each group):


.. ipython:: python

    def getGroups(loonplot):
        if (not isinstance(loonplot, loon)): 
            print("loonplot must be an l_plot")
        unique_cols = np.unique(loonplot['color'])
        res = [loonplot['color'] == x for x in unique_cols]
        return res;

    myGroups = getGroups(p)    # returns groups identified by unique colour in p
    nGroups = len(myGroups) # number of groups
    group1 = myGroups[0]     # each group is an element of the list myGroups;

Similarly, other point symbol characteristics (e.g. `size`, `glyph`) might be used to define groups.  This is particularly handy when these are first determined interactively.

--- 

setting plot contents
^^^^^^^^^^^^^^^^^^^^^^^

In addition to accessing the state values of a loon plot using `[]`, its values may also be set using `[]`.  For example, try these:


.. ipython:: python

    import random
    import time 
    p["showGuides"] = True

    p["size"] = random.choices(range(30),k=len(p['x']))


    p["selected"] = myGroups[0]
    p["selected"] = myGroups[1]


    p["selected"] =  False

    # something a little more involved for up to 6 groups
    myCols = ["firebrick", "steelblue", "purple", 
                "orange", "grey10", "grey80"]
    for i in range(len(myGroups)):
        p["color"][myGroups[i]] = myCols[i]
    
    # something crazy
    for j in range(10):
        p['xTemp'] = p['x'] + np.random.uniform(-0.5,0.5,len(p['x']))
        time.sleep(1)

    # putting locations and size back
    
    p["xTemp"] = p["x"]
    p["size"] = 4;

--- 


Adding layers
~~~~~~~~~~~~~~~
`loon` plots are actually a little richer still.  The scatterplot is only one possible layer in a plot.  It could have many more, each layer having different geometric objects.

---

Example: adding maps
^^^^^^^^^^^^^^^^^^^^^
For example, we can add a map to the current loon plot `p`.

First get the relevant map:

~~~~~~~~~~~~~~~~~~~~
```{r gettingAMap}
library(maps)
NZFijiMap <- map("world2", 
                 regions=c("New Zealand", "Fiji"),
                 plot=FALSE)
```


It is added as a "layer" to the loon plot


```{r addingAMap,  eval = TRUE, echo = TRUE, fig.align="center", fig.width = 5, fig.height = 5, out.width = "75%", warning=FALSE, message=FALSE, tidy = FALSE}
l_layer(p, NZFijiMap, 
        label = "New Zealand and Fiji",
        color = "forestgreen",
        index = "end")
```


Try this out. 


```{r quakesGuidesMapInspector, out.width= "30%", fig.align="center", echo=FALSE}
knitr::include_graphics(path_concat(imageDirectory, "quakesGuidesMapInspector.png"))
```

```{r quakesGuidesMap, out.width= "50%", fig.align="center", echo=FALSE}
knitr::include_graphics(path_concat(imageDirectory, "quakesGuidesMap.png"))
```

As can be seen in the world view, much of the map is outside of the plot display (shown as the black-bordered rectangle in the world view).

Now play with the scaling buttons in the loon inspector.

---

### 3.5.2. Effect of scaling choices


Adding the map allows us to see the effect of all three plot scaling choices available in the inspector.

The effect is best seen on the world view:

```{r worldViewScaling, out.width= "90%", fig.align="center", echo=FALSE}
knitr::include_graphics(path_concat(imageDirectory, "quakesWorldViewScaling.png"))
```

Note that the plot in the world view matches that of the actual plot.  Also the aspect ratio changes with the scaling.


---

### 3.5.3. the "Layers" tab

The map is added as a layer, which can be seen by selecting the "Layers" tab in the inspector:

```{r quakesLayersInspector, out.width= "70%", fig.align="center", echo=FALSE}
knitr::include_graphics(path_concat(imageDirectory, "quakesLayersInspector.png"))
```

This allows a lot of interaction with the layers - for example changing their display order, making some of them invisible, grouping layers, and so on.

---

## 3.6. Syntax: loon's `l_plot()` is like base graphics `plot()`


`loon`'s `l_plot()` syntax **intentionally resembles** that of `plot()` from the base `graphics` package:


```{r loon and base syntax, eval = FALSE, echo = TRUE, fig.align="center", fig.width = 6, fig.height = 5, out.width = "75%", warning=FALSE, message=FALSE, tidy=FALSE}

# 6. Base graphics
plot(x = quakes$long, y = quakes$lat, 
     xlab = "longitude", ylab = "latitude",
     main = "Tonga trench earthquakes")

# 7. loon graphics
l_plot(x = quakes$long, y = quakes$lat, 
       xlabel = "longitude", ylabel = "latitude",
       title = "Tonga trench earthquakes")
```


The arguments to `l_plot()` provide initial values to each named state.  Note that the argument names in `l_plot` are slightly different.

In result, however, loon plots are quite different

-  displays **look different**
- `l_plot()` **returns a data structure**; `plot()` does not
    - a rich data structure with many states
    - can be transformed to a grob
- the `loon` plot is **highly interactive**
    - either from the inspector
    - or programmatically
    
In loon, the function `plot.loon()` is a **method** of the base `plot()` generic function
that turns the loon plot (as the first argument of `plot.loon()`) into a grid object and plots it on the current `R` graphics device.

---

# 4. `l_hist()` the `loon` histogram

As seen earlier, the `quakes` data has some other variates in addition to the latitude and longitude of the quakes.

Before starting, make sure that you have the four groups coloured in the loon plot `p` as described earlier.  If you don't, then colour them again now.

Let's consider a histogram of the `depth` of each earthquake.


```{r histogram of magnitude,  eval = TRUE, echo = TRUE, fig.align="center", fig.width = 5, fig.height = 5, out.width = "75%", warning=FALSE, message=FALSE, tidy = FALSE}
h <- l_hist(quakes$depth, 
            xlabel = "depth", 
            title = "Tonga trench earthquakes")
```


Note that the inspector has changed.  There is a different inspector for each type of base loon plot.

**Exercise**: 

- in the plot section of the histogram inspector, select `yshows: density`
- on the histogram, see how individual bars can be selected
- what happens when you modify the colour?
- on the histogram, what is the (interactive) function of the small grey object?
    - how can you make it go away?
- on the histogram inspector, turn on stacked colours
- select colours on the histogram


---

# 5. Linking 

Now that we have both a scatterplot and a histogram, we can explore one of the most important features of an interactive data visualization system like loon.

## 5.1. `linkingGroup`

The principal feature of loon plots which effect the linking of displays is the setting of a common `linkingGroup`.

-  On the histogram inspector, where it says linking group, select the text "none" and replace it with "quakes"

- On the scatterplot inspector, if you do the same you will now be prompted to either "push" or "pull".  Select "push".

- **NOTE**: Programmatically, we might have tried to set the linking group directly on the plot as

    ```{r set linkingGroup mistake, eval = FALSE, warning=FALSE, message=FALSE, tidy = FALSE}
    h["linkingGroup"] <- "quakes"
    p["linkingGroup"] <- "quakes"
    ```
    
    but **this would have resulted in an error**.  The problem is that the synchronization must be set at the same time to determine where the linked states are to be drawn from. 
    To effect this, the loon command `l_confiure()` must be used whenever **two or more states are to be set simultaneously**.
    The correct programmatic setting of the "linkingGroup" is 
    ```{r fix colors again, eval = TRUE, fig.align="center", fig.width = 6, fig.height = 5, out.width = "60%", warning=FALSE, message=FALSE, tidy = FALSE}
    l_configure(h, linkingGroup = "quakes", sync = "push")
    l_configure(p, linkingGroup = "quakes", sync = "pull")
    ```
    
    This causes `h` to push its linked states to the "quakes" group and `p` to pull them from the "quakes" group. (In this example, "pull" could have been used in both cases and is generally recommended.)

- brush the scatterplot and observe the effects in the histogram

- brush the histogram and observe the effects in the scatterplot
    - shape the brush so that it is tall and thin
    - brush from left to right and right to left (i.e. from shallow to deeper earthquake depths)
    
- could also set colours programmatically on the histogram. Here we colour the histogram bars so that those earthquakes that are deepest are darkest.

    ```{r histogram blues, fig.align="center", fig.width = 7, fig.height = 5, out.width = "60%", warning=FALSE, message=FALSE, tidy = FALSE}
    blues5 <- blues9[c(2,4,6,8,9)] # select 5 from light blue to dark
    h["color"] <- blues5[cut(quakes$depth, breaks=5)] # assign colours by depth
    p["glyph"] <- "ccircle"
    p["showGuides"] <- TRUE
    # plot(p) # will print the plot
    ```

---

## 5.2. linking many plots

Arbitrarily many plots may be created and linked in loon.

Consider, for example, adding two more histograms to the same `linkingGroup`.  Note that the linking is done at creation and that the synchronization is by default a "pull".


```{r final quakes histograms, fig.align="center", fig.width = 5, fig.height = 5, out.width = "75%", warning=FALSE, message=FALSE, tidy = FALSE}
h_mag <- l_hist(x = quakes$mag, 
                linkingGroup = "quakes", 
                showStackedColors = TRUE,
                yshows = "density",
                xlabel = "magnitude")

h_stations <- l_hist(x = quakes$stations, 
                     linkingGroup = "quakes", 
                     showStackedColors = TRUE,
                     yshows = "density",
                     xlabel = "Number of stations reporting")
```



Brush to show the relationship between magnitude of the earthquake and the number of stations reporting.

Alternatively, we could look at a linked scatterplot of these two variates and explore their relationship conditional on `depth`

```{r final quakes plot, fig.align="center", fig.width = 5, fig.height = 5, out.width = "75%", warning=FALSE, message=FALSE, tidy = FALSE}
p_mag_stations <- l_plot(x = quakes$mag, 
                         y = quakes$stations, 
                         showGuides = TRUE,
                         glyph = "ccircle",
                         linkingGroup = "quakes", 
                         xlabel = "Magnitude", 
                         ylabel = "Number of stations reporting")
```

Brushing any one of these plots will cause the other plots to highlight in response.

Note that selection effectively shows the relations in one plot  **conditional** upon the values actively being selected (e.g. brushed) in another.


## 5.3. `linkingKey`

Observations in a `loon` plot are uniquely identified (for the purpose of linking) by their `linkingKey`. Pardon the pun but this is the key to linking in `loon`.

For the most part, the default linking is all that you ever need do.  
Trouble may arise, however, if you want to link two different plots that were created with different data frames whose rows so not match row for row. For example, one `data.frame` might be a re-ordering of the rows of the other. Or, it might be a subset of the rows of the other.

In either case, to have linking work properly the `linkingKey` of the plots associated with the two data frames need to be managed.

For example, 

```{r, eval = FALSE}
new_order <- sample(1:nrow(quakes), nrow(quakes), replace = FALSE)
some_quakes <-  sample(1:nrow(quakes), 100, replace = FALSE)
quakes_linkingKey <- p["linkingKey"]
p_new <- with(quakes[new_order,],
              l_plot(long, lat, title = "quakes reordered",
                     linkingGroup = "quakes",
                     linkingKey = quakes_linkingKey[new_order] ))
p_subset <- with(quakes[some_quakes,],
              l_plot(long, lat, title = "quakes reordered",
                     linkingGroup = "quakes",
                     linkingKey = quakes_linkingKey[some_quakes]))
```

The new plots `p_new` and `p_subset` will link correctly with all the rest.

Rather than the default values, the `linkingKey` can be any vector of unique strings used in any newly created plot as above.  Of course, not using the default linking keys from `loon` may require a little more care in management from the user.


---

# 6. Three dimensional plots - `l_plot3D`

Given that the `quakes` data has three spatial dimensions (`long`, `lat`, and `depth`), it would be natural to view this in a three dimensional scatterplot.

```{r plot_3D,  fig.align="center", fig.width = 5, fig.height = 5, out.width = "75%", warning=FALSE, message=FALSE, tidy = FALSE}

# 8. First, scale the data
scaled_quakes <- l_scale3D(quakes)

p_mag_stations <- l_plot3D(x = scaled_quakes$long,  
                           y = scaled_quakes$lat, 
                           z = scaled_quakes$depth, 
                           showGuides = TRUE,
                           linkingGroup = "quakes", 
                           title = "Three dimensional plot of quakes")
```

Select the plot, type `r` to turn on the `rotation mode`.   Press the down arrow on the keyboard until the darkest points (deepest quakes) are at the bottom of the display.   Press `r` again to turn off the rotation mode.

Selecting the plot, the key `r` toggles the rotation mode; arrow keys rotate the plot vertically and horizontally.  In `rotation mode` the plot may also be rotated free hand using the mouse. 
When `rotation mode` is toggled off (with the key `r`), the plot can again be brushed et cetera as with any `l_plot`.  See `help("l_plot3D")` for more details.


**NOTE** Many methods exist for visualizing higher dimensional data in `loon`.  For e.g. see `help("l_navgraph")`, `help("l_pairs")`, or `help("l_serialaxes")`.  See also the online manual `l_web()`.


---

# 7. Extras

Miscellaneous other topics on and sources of working and programming with `loon`.

---

## 7.1. More examples

Being able to get and set the plot contents means that it is possible to capture different
plot states as `grobs`. 
There are a variety of ways to see how you might put `loon` to use.

There are of course many smaller examples available through the `loon`'s `R` documentation available via
```{r, eval=FALSE}
help(package = "loon")
```
and more complex examples and more general discussion via `loon`'s online help
```{r, eval=FALSE}
l_help()

# 9. or more simply via the online manual
l_web()
```

---

### 7.1.1. Other vignettes

Other vignettes have been developed to cover a range of topics.  These currently include:

- An example exploratory analysis: "Visible minorities in Canadian cities" available via
    ```{r, eval=FALSE}
    vignette("minorities", package = "loon")
    ```
    This illustrates a variety of `loon` features including map layers, parallel coordinate axes, and radial axes glyphs in the context of an exploratory analysis of the distribution of visible minorities in 33 Canadian cities.
    
- New interactive graphics in `loon` in a teaching example: "Smoothers and Bone Mineral Density" available via
    ```{r, eval=FALSE}
    vignette("teaching-example-smoothing", package = "loon")
    ```
    This illustrates how to create new interactions in `loon` through more general bindings.  This is done by developing a teaching tool for explaining how smoothing works.  The example data set is `bone` from the `ElemStatLearn` package. 

- Some suggestions on integrating `loon` plots into an Rmarkdown document: "Loon in RMarkdown" via
    ```{r, eval=FALSE}
    vignette("Rmarkdown", package = "loon")
    ```
       
---

### 7.1.2. loon demos

There are numerous demos in loon whose source code might be examined for more examples of using `loon`.  To see them all

```{r loon demos, eval = FALSE}
demo(package = "loon")  # list all demos
```

The range is quite broad.  For example, 

```{r loon demo examples, eval = FALSE}

### 9.1. teaching demos
demo("l_regression", 
     package = "loon")  # lots using the Old Faithful geyser
demo("l_regression_influential", 
     package = "loon")  # move and recolor points to change the regression fit

### 9.2. gapminder
demo("l_us_and_them", 
     package = "loon")  #  basic demo
demo("l_us_and_them_slider", 
     package = "loon")  # year selected on a slider
demo("l_us_and_them_choropleth", 
     package = "loon")  # world map and linked with a scatterplot

### 9.3. the spatial package sp                       
demo("l_polygons_sp", 
     package = "loon")  # layer polygons with class sp 

### 9.4. layering and custom layouts 
demo("l_layers")  # demonstrate layer types   
demo("l_layout")  # custom layout widgets      
demo("l_widgets") # inspector and plot in one window

### 9.5. novel brushing and linking 
demo("l_knn")     # brushing by k nearest points in some subspace
demo("l_us_and_them_choropleth")  # many to one linking 

### 9.6. high dimensional data and dimensionality reduction
demo("l_ng_images_frey_LLE") # navigation graphs, image data, LLE
demo("l_ng_dimred")          # comparing dimension reduction methods
```

The code that appears in the console after the demo can be examined and reused to create your own loony `loon` code.

---

## 7.2. Extensions to loon via other packages

### 7.2.1. `zenplots` 

This package is available on CRAN. 
```{r, eval=FALSE}
install.packages("zenplots")
vignette("intro", package = "zenplots")
```

Provides a means for compact layout of alternating 1d (e.g. histograms) and 2d (e.g. scatterplots)  plots.  In will layout base `graphics` plots, `grid` graphics plots, and `loon` plots.

It is similar to `pairs` plots but allows many many more plots to be displayed.  From the introductory vignette:

> "A zenplot can show the same information as a pairs plot but with two important display differences.
>
>First, the matrix organization of the pairs layout is replaced by the “zig-zag” layout of zenplot. Second, the number of plots produced is about half that of a pairs plot allowing each plot in a zenplot to be given more visual space."

### 7.2.2. Specialty `loon` extensions -  `loon.<specialty>` packages

There are/will be other packages available which build on `loon`.  Those developed by us are typically prefixed with `loon` (e.g. `loon.ggplot`)

These will typically be on CRAN when ready, but development versions are accessible from our various `github` repositories. For example,

- [https://github.com/rwoldford](https://github.com/rwoldford)
- [https://github.com/waddella](https://github.com/waddella)

There you can see what is coming up.

---

## 7.3. More on grid graphics and loon

Graphics in the `grid` package are built up from graphical objects or `grobs`.

In `loon`, the functions `grid.loon()` and `loonGrob()` construct `grobs` from loon plots which can then be used as any other `grob` in `grid`

For example, when transformed to `grid`,  the loon plot `p` structure becomes a `gTree` in `grid`.


```{r grid grob, eval = TRUE, echo = TRUE, fig.align="center", fig.width = 5, fig.height = 5, out.width = "75%", warning=FALSE, message=FALSE, tidy = FALSE}
gp <- loonGrob(p)
gp
```

This simply produces the grid data structure corresponding to the current state of the loon plot `p`, as can be seen from listing its contents:

```{r list grid grob, eval = FALSE}
library(grid)
grid.ls(gp)  # lists the contents of the grob
```

The grob `gp` could now be used with all the functionality of the `grid` package.  

Note that all of the elements of a loon plot appear in the grob, either explicitly or, if they were not drawn in the loon plot, as an empty `grob` containing the relevant arguments to drawing them.

Another function in loon to help that is the `grid.loon()` function
```{r grid graphic display loon plot, eval = FALSE, echo = TRUE, fig.align="center", fig.width = 5, fig.height = 5, out.width = "75%", warning=FALSE, message=FALSE, tidy = FALSE}
library(grid)
grid.newpage()
grid.loon(p)
```

will display `p` as a  `grid` graphic ... and all that entails.
