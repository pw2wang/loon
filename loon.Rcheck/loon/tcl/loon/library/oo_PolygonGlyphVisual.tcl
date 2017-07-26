
oo::class create loon::classes::PolygonGlyphVisual {
    
    superclass  ::loon::classes::GlyphVisual
    
    variable x_var y_var n_var linewidth_var showArea_var
    
    constructor {GlyphObject args} {

	set ns [info object namespace $GlyphObject]
	set x_var [${ns}::my varname x]
	set y_var [${ns}::my varname y]
	set n_var [${ns}::my varname n]
	set linewidth_var [${ns}::my varname linewidth]
	set showArea_var [${ns}::my varname showArea]

	next $GlyphObject {*}$args
	
    }
    
    method draw {canvas ind} {
	my variable glyphObject
	
	
	set id [uplevel #0 $canvas create polygon 0 0 0 0\
		    -width [lindex [set $linewidth_var] $ind]]
	
	return $id
    }
    
    
    method updateCoords {id canvas ind size} {
	my variable glyphObject

	set factor [::loon::map_polygon_size $size]
	
	$canvas coords $id\
	    {*}[::loon::listfns::interleave\
		    [lmap x [lindex [set $x_var] $ind] {expr {$x*$factor}}]\
		    [lmap y [lindex [set $y_var] $ind] {expr {$y*$factor}}]]	
	
    }


    method recolor {id canvas ind color} {
	if {[lindex [set $showArea_var] $ind]} {
	    $canvas itemconfigure $id -fill $color -outline $color
	} else {
	    $canvas itemconfigure $id -fill "" -outline $color
	}
    }
    
}
