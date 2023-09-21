# Twitter_community_detection
##Twitter User Clustering using DBSCAN, hierarchical, and Spectrul
This code performs clustering of Twitter users based on their follower-followee relationships using the Density-Based Spatial, hierarchical, and Spectrul Clustering of Applications. The primary objective is to group users into clusters that share similar interaction patterns within the Twitter network.

#Files and Directory Structure
glob: Python module used for filename pattern matching.
pickle: Python module for serializing and deserializing Python objects.
networkx: Python library for the creation, manipulation, and study of complex networks.
sklearn.cluster.DBSCAN: DBSCAN implementation from scikit-learn, used for clustering.
tqdm: Python module for displaying progress bars.
aggregatedRounds/: Directory containing aggregated follower-followee data for multiple rounds.
round1/Tweets/: Directory containing tweets data for round 1.
community/: Directory to store clustering results.
How the Code Works
Data Preparation:
Retrieves user IDs from the provided tweet data directory.
 ##Clustering:
Iterates through rounds (1 to 15) of follower-followee data.
Constructs a directed graph representing user relationships (followers and followees).
Computes the adjacency matrix from the graph.
Applies DBSCAN clustering using the adjacency matrix.
Clustering Results:
Saves the clustering results (cluster labels) for each round in the community/ directory.
#Usage
Ensure you have the necessary Python modules installed.
Place your Twitter user data in the appropriate directories as per the expected structure.
Run the code to perform DBSCAN clustering and obtain clustering results for each round.
For any inquiries or issues, please feel free to reach out.
