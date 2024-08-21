from matplotlib import pyplot as plt
from matplotlib.sankey import Sankey

# Create a sequence diagram using Sankey plot to simulate the flow
Sankey(flows=[1, -1, 1, -1, 1, -1, 1, -1, 1],
       labels=['Start Research', 'Access Web Browser', 'Use Language Model', 'Receive Suggestions',
               'Access Data Sources', 'Evaluate Data Sources', 'Collect Data', 'Finalize List', 'End'],
       orientations=[0, 1, 0, 1, 0, 1, 0, 1, 0]).finish()

plt.title('Sequence Diagram for Research and Data Sourcing Task')
plt.show()
