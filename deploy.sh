#/bin/bash
for file in deployment/*; do
envsubst < "$file" | kubectl apply -n app -f -
done

