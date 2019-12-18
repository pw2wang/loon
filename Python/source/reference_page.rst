Reference 
=================

Package Information
-------------------------
desc:  General Information about the package
contents:

- loon
- :mod:`l_help`
- :mod:`l_web`

Main Plotting Functions
-------------------------
desc:  These are the main functions needed to create plots
contents:

- :mod:`diver.l_plot`
- :mod:`diver.l_hist`
- :mod:`diver.l_plot3D`
- :mod:`diver.l_pairs`
- :mod:`diver.l_serialaxes`

Access Modify
-------------------------
desc: Access Modify
contents:

- :mod:`diver.l_cget`
- :mod:`diver.l_configure`
- :mod:`diver.l_info_states`
- :mod:`diver.l_state_names`
- :mod:`diver.l_getLinkedStates`
- :mod:`diver.l_setLinkedStates`
- :mod:`diver.l_getOption`
- :mod:`diver.l_setOption`
- :mod:`diver.l_userOptions`
- :mod:`diver.l_getOptionNames`
- :mod:`diver.l_getPlots`
- :mod:`diver.l_scale`
- :mod:`diver.l_move`
- :mod:`diver.l_redraw`
- :mod:`diver.l_size`
- :mod:`diver.l_zoom`
- :mod:`diver.l_copyStates`
- :mod:`diver.l_saveStates`

Miscellaneous
-------------------------
desc: Miscellaneous
contents:

- :mod:`diver.l_resize`
- :mod:`diver.l_export`
- :mod:`diver.l_export_valid_formats`
- :mod:`diver.l_aspect`
- :mod:`diver.l_setAspect`
- :mod:`diver.l_subwin`
- :mod:`diver.l_widget`
- :mod:`diver.l_setTitleFont`
- :mod:`diver.l_getLocations`
- :mod:`diver.l_userOptionDefault`

Colors
-------------------------
desc: Colors
contents:

- :mod:`diver.color_loon`
- :mod:`diver.tkcolors`
- :mod:`diver.hex12tohex6`
- :mod:`diver.l_hexcolor`
- :mod:`diver.l_getColorList`
- :mod:`diver.loon_palette`
- :mod:`diver.l_colRemoveAlpha`
- starts_with("l_setColor")

Layering
-------------------------
desc: Layers
contents:
- :mod:`diver.l_layer`


Glyphs
-------------------------
desc: Glyphs
contents:

- starts_with("l_glyph")
- l_primitiveGlyphs
- starts_with("l_image")
- l_make_glyphs

Bindings
-------------------------
desc: Bindings
contents:

- starts_with("l_bind")
- starts_with("l_current")
- l_after_idle

Graph
-------------------------
desc: Graph
contents:

- :mod:`diver.l_graph`
- :mod:`diver.complement`
- :mod:`diver.complement.loongraph`
- :mod:`diver.completegraph`
- :mod:`diver.graphreduce`
- :mod:`diver.loongraph`
- :mod:`diver.linegraph`
- :mod:`diver.linegraph.loongraph`
- :mod:`diver.l_getGraph`
- :mod:`diver.ndtransitiongraph`

Navigation Graphs
-------------------------
desc: Navigation
contents:

- starts_with("l_ng")
- starts_with("l_nav")
- l_create_handle

Contexts
-------------------------
desc: Contexts are
contents:
- starts_with("l_context")

Grid Grobs
-------------------------
desc: Grid Grobs
contents:

- :mod:`diver.loonGrob`
- :mod:`diver.grid.loon`
- :mod:`diver.condGrob`
- :mod:`diver.l_createCompoundGrob`
- :mod:`diver.l_get_arrangeGrobArgs`
- :mod:`diver.loonGrob_layoutType`

Data
-------------------------
desc: data
contents:

- :mod:`diver.UsAndThem`
- :mod:`diver.olive`
- :mod:`diver.oliveAcids`
- :mod:`diver.oliveLocations`
- :mod:`diver.minority`

Inspectors
-------------------------
desc: inspectors
contents:

- ends_with("inspector")
- diver.l_hist_inspector_analysis
- diver.l_worldview

Others
-------------------------
desc: others
contents:

- :mod:`diver.l_list2nestedTclList`
- :mod:`diver.l_nestedTclList2list`
- :mod:`diver.l_data`
- :mod:`diver.l_throwErrorIfNotLoonWidget`
- :mod:`diver.l_toR`
- :mod:`diver.l_isLoonWidget`
- :mod:`diver.L2_distance`

Measures
-------------------------
desc: measures
contents:

- :mod:`diver.measures1d`
- :mod:`diver.measures2d`
- :mod:`diver.scagnostics2d`
- :mod:`diver.print.measures1d`
- :mod:`diver.print.measures2d`