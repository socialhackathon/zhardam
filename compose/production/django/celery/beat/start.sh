#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset


celery -A jardam_kolu.taskapp beat -l INFO
