import logging
import os

import subprocess

logger = logging.getLogger(__name__)


class Combiner(object):
    def __init__(self, options):
        self.options = options

    def combine(self, page_file_names):
        output_file_name = self.options.output_file_name[0]
        logger.info("combine %d pages into %s", len(page_file_names), output_file_name)
        combine_args = ['pdftk']
        combine_args += page_file_names
        combine_args += ['output', os.path.basename(output_file_name), 'compress']
        returncode = subprocess.call(combine_args)

        if returncode != 0:
            logger.error("combine failed: %s", " ".join(combine_args))

        return returncode
