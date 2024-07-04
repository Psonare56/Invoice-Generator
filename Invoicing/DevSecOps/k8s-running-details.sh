#!/bin/bash

NAMESPACE="invoice-generator-namespace"

echo "Fetching secrets in namespace $NAMESPACE"
kubectl get secret -n $NAMESPACE

echo "Fetching pods in namespace $NAMESPACE"
kubectl get pods -n $NAMESPACE

echo "Fetching deployments in namespace $NAMESPACE"
kubectl get deployment -n $NAMESPACE

echo "Fetching services in namespace $NAMESPACE"
kubectl get svc -n $NAMESPACE

echo "Fetching namespaces"
kubectl get namespace 

echo "Fetching StatefulSets in namespace $NAMESPACE"
kubectl get statefulset -n $NAMESPACE 

echo "Fetching DaemonSets in namespace $NAMESPACE"
kubectl get daemonset -n $NAMESPACE

echo "Fetching ConfigMaps in namespace $NAMESPACE"
kubectl get configmap -n $NAMESPACE

echo "Fetching PersistentVolumeClaims in namespace $NAMESPACE"
kubectl get pvc -n $NAMESPACE

echo "Fetching PersistentVolumes"
kubectl get pv

echo "Fetching Horizontal Pod Autoscalers in namespace $NAMESPACE"
kubectl get hpa -n $NAMESPACE

echo "Fetching Vertical Pod Autoscalers in namespace $NAMESPACE"
kubectl get vpa -n $NAMESPACE

echo "Fetching ingresses in namespace $NAMESPACE"
kubectl get ingress -n $NAMESPACE

echo "Describing ingress invoice-generator-ingress in namespace $NAMESPACE"
kubectl describe ingress invoice-generator-ingress -n $NAMESPACE

echo "Fetching logs for Ingress controller pods in ingress-nginx namespace"
kubectl logs -l app.kubernetes.io/name=ingress-nginx -n ingress-nginx  # Adjust the label selector if needed

echo "Script execution completed."
