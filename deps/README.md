# Dependencies

Spin up at least 16 [CloudLab m510 machines](https://docs.cloudlab.us/hardware.html). 
For the CloudLab profile that we followed, see `profile.py`.

Choose one node to be the driver node (we choose `node-0`, according to our profile), run:
```
sudo su
git clone https://github.com/jl3953/install_everything
./ssh_all_nodes_main.py 16 # replace 16 with the number of nodes you spun up.

```

Note: `node-11`, `node-12`, and `node-13` are special and always reserved
for running Cicada, the single-machine database serving as the turbo.
