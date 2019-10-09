#!/bin/bash

set_env() {
    export TWINE_USERNAME=victorziv
    export TWINE_PASSWORD=Bab1848uin
    export TWINE_REPORSITORY=testpypy
    export TWINE_REPOSITORY_URL=https://test.pypi.org/legacy/
}
# ______________________________________

run_tests() {
    pytest -v tests/
    if [ $? -ne 0 ];then
        echo "Failure in testing, cannot proceed"
        exit 42 
    fi
}
# ______________________________________

publish() {
    python setup.py publish
}
# ______________________________________

main() {
    set_env
    make venv
    make init
    source venv/bin/activate
#    run_tests
    make ci
    make publish
}
# ______________________________________

main "$@"
