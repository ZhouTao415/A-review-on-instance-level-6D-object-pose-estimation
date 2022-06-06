# Added a new paper to the list.
# Author: Yinyu Nie
# Updated data: 23 June, 2021
import argparse

existing_topics = ['Pose Estimation',
                   'Others',
                   'Survey, Resources and Tools']


class ParseKwargs(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, dict())
        for value in values:
            key, value = value.split('=')
            getattr(namespace, self.dest)[key] = value
