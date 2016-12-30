# WLokalu: an application showing presence in HS premises.

This application is developed with HS:Wrocław in mind, so the interface is in
Polish only. It might come in English in near future.


## Running locally

    cd path/to/this/repo
    pip install Django==1.4
    ./manage.py runserver


## Using the API

To get available methods:

    curl -XGET -w\\n http://127.0.0.1:8000/api/v1/

To send seonsor info:

    curl -XPOST -w\\n http://127.0.0.1:8000/api/v1/sensor/your_sensor_name -d '{"state":"foobar"}'


## License

This software is released under the GPL version 3. See LICENSE for details.
