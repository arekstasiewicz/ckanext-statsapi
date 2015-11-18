import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.logic as logic
from ckan.lib.base import BaseController
from logging import getLogger
from ckan.plugins.toolkit import Invalid
from ckan.lib.base import BaseController
from ckan.common import json, response, request
import ckanext.stats.stats as stats_lib
import ckan.lib.formatters as formatters
import ckan.lib.helpers as core_helpers
import ckan.model as model
import os

log = getLogger(__name__)

class StatsapiPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)
    plugins.implements(plugins.IPackageController, inherit=True)

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'statsapi')

    # IRoutes
    @staticmethod
    def after_map(m):
         m.connect('datasetcount', '/api/3/stats/dataset_count',
            controller='ckanext.statsapi.plugin:StatsApi', action='dataset_count')

         m.connect('groupcount', '/api/3/stats/group_count',
            controller='ckanext.statsapi.plugin:StatsApi', action='group_count') 

         m.connect('organizationcount', '/api/3/stats/organization_count',
            controller='ckanext.statsapi.plugin:StatsApi', action='organization_count')

         m.connect('topratedpackages', '/api/3/stats/top_rated_packages',
            controller='ckanext.statsapi.plugin:StatsApi', action='top_rated_packages')

         m.connect('mosteditedpackages', '/api/3/stats/most_edited_packages',
            controller='ckanext.statsapi.plugin:StatsApi', action='most_edited_packages')

         m.connect('largestgroups', '/api/3/stats/largest_groups',
            controller='ckanext.statsapi.plugin:StatsApi', action='largest_groups')

         m.connect('toptags', '/api/3/stats/top_tags',
            controller='ckanext.statsapi.plugin:StatsApi', action='top_tags')

         m.connect('toppackagecreators', '/api/3/stats/top_package_creators',
            controller='ckanext.statsapi.plugin:StatsApi', action='top_package_creators')

         return m

        
class StatsApi(BaseController):

    def dataset_count(self):
        response.content_type = 'application/json; charset=UTF-8'
        count = str(logic.get_action('package_search')({}, {"rows": 1})['count'])
        data = {"dataset_count" : count}
        return json.dumps(data)

    def group_count(self):
        response.content_type = 'application/json; charset=UTF-8'
        count = len(logic.get_action('group_list')({}, {}))
        data = {"group_count" : count}
        return json.dumps(data)

    def organization_count(self):
        response.content_type = 'application/json; charset=UTF-8'
        count = len(logic.get_action('organization_list')({}, {}))
        # changes '000' to 'k' for numbers greater than 1000
        data = {"organization_count" : formatters.localised_SI_number(count)}
        return json.dumps(data)




    def top_rated_packages(self):
        response.content_type = 'application/json; charset=UTF-8'
        count = 0
        data = {"top_rated_packages" : count}
        return json.dumps(data)

    def most_edited_packages(self):
        response.content_type = 'application/json; charset=UTF-8'
        count = 0
        data = {"most_edited_packages" : count}
        return json.dumps(data)

    def largest_groups(self):
        response.content_type = 'application/json; charset=UTF-8'
        count = 0
        data = {"largest_groups" : count}
        return json.dumps(data)

    def top_tags(self):
        response.content_type = 'application/json; charset=UTF-8'
        count = 0
        data = {"top_tags" : count}
        return json.dumps(data)

    def top_package_creators(self):
        response.content_type = 'application/json; charset=UTF-8'
        count = 0
        data = {"top_package_creators" : count}
        return json.dumps(data)

