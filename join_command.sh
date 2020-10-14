#!/bin/bash
# This should be the output of "kubeadm token create --print-join-command" on your k8.
# Upload this file to your s3 so the newly create instance can access and excecute it on the first run.

kubeadm join 172.31.100.100:6443 --token 0bsdfsdfdsfdsfsdfsdfsdfds \
    --discovery-token-ca-cert-hash sha256:sdfsdfsdfsdfsdfsdfsdfsdfdsfsdfdsfdsfsdfsdfsdfdsfdsfdsfdsfsdsdf
