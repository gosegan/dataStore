#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from webapp2_extras import jinja2
from time import gmtime, strftime
from webapp2_extras.users import users


class Person(object):
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class MainHandler(webapp2.RequestHandler):
    def __init__(self, request=None, response=None):
        super(MainHandler, self).__init__(request, response)

    def get(self):
        usr = users.get_current_user()

        if usr:
            login_logout_url = users.create_logout_url("/")
        else:
            login_logout_url = users.create_login_url("/")

        people_list = [
            Person('Denys', 'Danylko', 18),
            Person('Serhii', 'Konar', 19),
            Person('Daniil', 'Novik', 20)
        ]
        plantilla_sust = {
            "login_logout_url": login_logout_url,
            "usr": usr,
            "fecha": strftime("%Y-%m-%d", gmtime()),
            "hora": strftime("%H:%M:%S", gmtime()),
            "people": people_list
        }
        jinja = jinja2.get_jinja2(app=self.app)

        self.response.write(
            jinja.render_template("index.html", **plantilla_sust))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
