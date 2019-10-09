#!/bin/bash

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
    run_tests
    publish
}
# ______________________________________

main "$@"
