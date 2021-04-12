# About

This repository contains the Helm charts installation for a subset of LitmusChaos Experiments. For the moment the charts support installation of the following experiments:

* container-kill
* pod-memory-hog
* pod-network-latency

The installation is optimised for OpenShift, as it includes the the *SecurityContextConstraing* resource required for running LitmusChaos experiments that need elevated privileges. 

In order to not provide un-necessary permissions to experiments that don't require higher privileges, two Service Accounts will be deployed when using this chart: 
* `litmus-nonprivileged`: this will get non-privileged permissions and it will be used for experiments that don't require elevated privileges, i.e. *pod-memory-hog* experiment 
* `litmus-privileged`: for experiments requiring elevated privileges, i.e. *container-kill*, *pod-network-latency*

# How

A LitmusChaos installation is required before installing this chart. 

To deploy this chart, override the values.yaml file if necesarry, then run the following command:

```
helm install litmus-experiments helm/litmus-experiments
```