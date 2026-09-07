#!/bin/bash

#ADD an architecture specific bash script header here

mace_run_train \
    --name="MACE" \
    --foundation_model="$location_foundation_model/mace-mpa-0-medium.model" \
    --multiheads_finetuning=False \
    --train_file="trainingsset.xyz" \
    --valid_fraction=0.15 \
    --test_file="testset_MD.xyz" \
    --energy_weight=1.0 \
    --forces_weight=1.0 \
    --E0s="{"3": -201.709423776, "8": -431.6112445,"13": -52.880642, "15": -175.8879765038, "22": -1578.120396767 }" \
    --lr=0.001 \
    --scaling="rms_forces_scaling" \
    --batch_size=1 \
    --max_num_epochs=10 \
    --ema \
    --ema_decay=0.99 \
    --amsgrad \
    --default_dtype="float64" \
    --energy_key="REF_energy" \
    --forces_key="REF_forces" \
    --device=cpu \
    --seed=4 \
    --clip=10 \
    --restart_latest
