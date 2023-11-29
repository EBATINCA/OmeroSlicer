#
# Copyright (c) 2017 University of Dundee.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
import json
from datetime import datetime 

from omeroweb.decorators import login_required

# login_required: if not logged-in, will redirect to webclient
# login page. Then back to here, passing in the 'conn' connection
# and other arguments **kwargs.

   
@login_required()
def index(request, conn=None, **kwargs):
    
    # We can load data from OMERO via Blitz Gateway connection.
    # See https://docs.openmicroscopy.org/latest/omero/developers/Python.html
    
    #id image and date
    
    iids = request.GET.getlist('image')[0]
    now=str(datetime.now())

    #save JSON

    path='/home/Documents/slicer_volume/ids/'
    name_file=iids

    with open(path+name_file+'.json', "w") as outfile:
        json.dump({'id_image':iids,'upload_date':str(now)},outfile)
    

    # Redirect the html template and return the http response
    return redirect('http://192.168.1.79:6901/')