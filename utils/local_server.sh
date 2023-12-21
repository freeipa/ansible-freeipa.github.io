#!/bin/sh


if [ "$1" == "-h" ]
then
    echo -e "usage: local_serve.sh [-r] [-h]\n"
    cat <<EOM
      -h        Display this help message and exit.
      -r        Force container rebuild.
EOM
    exit 0
fi

SCRIPTDIR="$(realpath $(dirname $0))"
TOPDIR="$(dirname ${SCRIPTDIR})"

TAG="$(whoami)/ansible-freeipa_docs"

[ -d "${TOPDIR}/.vendor/bundle" ] || mkdir -p "${TOPDIR}/.vendor/bundle"

echo -n "Searching image... "
existing=$(podman images -f reference="localhost/${TAG}" --format "{{ .Repository }}")
echo "${existing:-NO}"

echo "Building image..."
[ "$1" == "-r" ] || [ -z "${existing}" ] && podman build -t "${TAG}" "${SCRIPTDIR}"

echo "Running container..."
podman run \
    --volume "${TOPDIR}:/srv/jekyll:Z" \
    --volume "${TOPDIR}/vendor/bundle:/usr/local/bundle:Z" \
    -p 4000:4000 \
    "${TAG}"

