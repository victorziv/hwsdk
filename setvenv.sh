#!/bin/bash

APP=hwsdk
ROOTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VENVDIR=$ROOTDIR/venv
# _________________________

install_modules() {
    cd ${ROOTDIR}
    source ${VENVDIR}/bin/activate
    cp "${ROOTDIR}/scripts/pip.conf" "${VENVDIR}/"
    pip install -r ${ROOTDIR}/requirements.txt
    deactivate

}
# _________________________

set_environment() {
    echo "export PYTHONPATH=${ROOTDIR}:${ROOTDIR}/${APP}" >> ${VENVDIR}/bin/activate
    echo "export FLASK_APP=$APP" >> ${VENVDIR}/bin/activate
    echo "export MAIL_SERVER=smtp-dev-telad.telad.il.infinidat.com" >> ${VENVDIR}/bin/activate
}
# _________________________

main() {
    rm -rf $VENVDIR
    virtualenv --python $(which python3.6) --no-site-packages --clear --verbose $VENVDIR
    set_environment
    install_modules
}
# _________________________

main "$@"
