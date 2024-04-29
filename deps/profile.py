"""Blank Ubuntu-20, populating 1TB dataset"""

#
# NOTE: This code was machine converted. An actual human would not
#       write code like this!
#

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg
# Import the Emulab specific extensions.
import geni.rspec.emulab as emulab
# Import the ProtoGENI library.
import geni.rspec.pg as rspec

# Create a portal object,
pc = portal.Context()

# Describe the parameter(s) this profile script can accept
pc.defineParameter("n", "Number of machines", portal.ParameterType.INTEGER, 12)
pc.defineParameter("firstNodeRWDataset", "Mount dataset in rw instead of rwclone on the first node", portal.ParameterType.BOOLEAN, False)

# Retrieve the values the user specifies during instantiation.
params = pc.bindParameters()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

# Check parameter validity.
if params.n < 1 or params.n > 255:
    pc.reportError(portal.ParameterError("You must choose at least 1 and no more than 255 machines."))
    

# Link link-0
link = request.Link('link-0')
link.Site('undefined')
link.best_effort = True
link.vlan_tagging = True
link.link_multiplexing = True

ifaces = []
for i in range(params.n):
    # Create a XenVM and add it to the RSpec.
    node = request.RawPC("node-" + str(i))
    node.hardware_type = 'm510'
    node.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU20-64-STD'
    bs = node.Blockstore("bs-" + str(i), "/data")
    bs.size = "150GB"
    bs.placement = "sysvol"
    node.addService(rspec.Execute(shell="bash", command="/usr/local/bin/setup"))
    
    iface = node.addInterface("interface-0", pg.IPv4Address("192.168.1." + str(i+1),'255.255.255.0'))
    link.addInterface(iface)
    
    # dataset
    iface_ds = node.addInterface()
    fsnode = request.RemoteBlockstore("fsnode" + str(i), "/mydata") # TODO: replace with your own dataset name
    fsnode.dataset = "urn:publicid:IDN+utah.cloudlab.us:cops-pg0+ltdataset+keyspace" # TODO: replace with your own cloudlab project name
    
    # The "rwclone" attribute allows you to map a writable copy of the
    # indicated SAN-based dataset. In this way, multiple nodes can map
    # the same dataset simultaneously. In many situations, this is more
    # useful than a "readonly" mapping. For example, a dataset
    # containing a Linux source tree could be mapped into multiple
    # nodes, each of which could do its own independent,
    # non-conflicting configure and build in their respective copies.
    # Currently, rwclones are "ephemeral" in that any changes made are
    # lost when the experiment mapping the clone is terminated.
    if (i > 0) or (not params.firstNodeRWDataset):
        fsnode.rwclone = True
    
    # Now we add the link between the node and the special node
    fslink = request.Link("fslink" + str(i))
    fslink.addInterface(iface_ds)
    fslink.addInterface(fsnode.interface)
    
    # Special attributes for this link that we must use.
    fslink.best_effort = True
    fslink.vlan_tagging = True
    fslink.link_multiplexing = True


# Print the generated rspec
pc.printRequestRSpec(request)
