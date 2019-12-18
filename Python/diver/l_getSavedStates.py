import pickle
from sys import exit
from .loon_class import loon_l_savedStates

def l_getSavedStates(file = None, **options):
    '''Retrieve saved plot states from the named file.    

    `l_getSavedStates` reads a file created by `l_saveStates()` containing
    the saved info states of a loon plot returning a loon object of class `loon_l_savedStates`.
    This is helpful, for example, when using some notebooking
    facility to recreate an earlier saved loon plot so as to present it
    in the document.
    Note that if the plot saved was an `loon_l_compound` then `l_getSavedStates`
    will return a dict of the plots with each list item being the saved states of the
    corresponding plots.

    Args:
        file: a connection or the name of the file where the `l_savedStates` python objecy
              is to be read from (as in `pickle.load()`).
        **optionsL furture augments passed to `pickle.load()`
    
    Returns:
        an object of class `loon_l_savedStates` containing the states and their values.

    See Also:
        `l_getSavedStates`, `l_copyStates`, `l_info_states`

    Examples:
        >>> # For compound plots, the info_states are saved for each plot
        >>> pp = l_pairs(iris)
        >>> myPairsFile = tempfile.NamedTemporaryFile(suffix = '.pkl').name
        >>> #
        >>> # Save the names states of pp
        >>> l_saveStates(pp,
        >>>             states = ["color", "active", "selected"],
        >>>             file = myPairsFile)
        >>> pairs_info =  l_getSavedStates(myPairsFile)
        >>> #
        >>> # For compound plots, the info states for all constitutent
        >>> # plots are saved.  The result is a list of class "l_savedStates"
        >>> # whose elements are the named plots as "l_savedStates"
        >>> # themselves.
        >>> #
        >>> # The names of the plots which were saved
        >>> pairs_info.get_savedname()
        >>> # And the names of the info states whose values were saved for
        >>> # the first plot
        >>> pairs_info['x1y0'].keys()
        >>> #
        >>> # square bracket notation [] has also been
        >>> # specialized to access to the contents of an l_savedStates object.
        >>> #
        >>> # For example,
        >>> p_saved_info["color"]
        >>> #
        >>> # returns the saved "color" as a vector of colours.
        >>> #
        >>> # In contrast,
        >>> pairs_info["x2y1"]
        >>> # returns the l_savedStates object of the states of the plot named "x2y1",
        >>> # but
        >>> pairs_info["color"]
        >>> # returns a dict of colour vectors, by plot as they were named in pairs_info
        >>> #
        >>> # As a consequence, the following two are equivalent,
        >>> pairs_info["x2y1"]["color"]
        >>> # finds the value of "color" from an "l_savedStates" object
        >>> # whereas
        >>> pairs_info["color"]["x2y1"]
        >>> # finds the value of "x2y1" from a "list" object
        >>> #
        >>> # Also, setting a state of an "l_savedStates" is possible
        >>> # (though not generally recommended; better to save the states again)
        >>> #
        >>> p_saved_info["color"] = ['red'] * 150
        >>> # changes the saved state "color" on p_saved_info
        >>> # whereas
        >>> pairs_info["color"] = ['red'] * 150
        >>> # will set the red color for any plot within pairs_info having "color" saved.
        >>> # In this way the assignment function via [] is trying to be clever
        >>> # for l_savedStates for compound plots and so may have unintentional
        >>> # consequences if the user is not careful.
        >>> # Generally, one does not want/need to change the value of saved states.
        >>> # Instead, the states would be saved again from the interactive plot
        >>> # if change is necessary.
    '''
    if(file == None):
        exit("missing name of file")      
    result = pickle.load(open(file,'rb'), **options)
    if(not isinstance(result,loon_l_savedStates)):
        exit('load object is not a loon_l_savedStates class object')
    return result 