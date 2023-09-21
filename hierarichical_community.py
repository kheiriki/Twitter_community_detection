{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import glob\
import pickle\
import networkx as nx\
from cdlib import algorithms\
from tqdm import tqdm\
\
users = glob.glob('round1/Tweets/*')\
users = [u.split('/')[-1].split('_')[0] for u in users]\
all_users = \{\}\
for u in users:\
    all_users[int(u)] = int(u)\
\
for round in tqdm(range(1, 16)):\
    round1_follower_followee = pickle.load(open('aggregatedRounds/round\{\}FriendFollowers.pkl'.format(round), 'rb'))\
    g = nx.DiGraph()\
    for u in tqdm(round1_follower_followee.keys()):\
        try:\
            h = all_users[int(u)]\
        except:\
            print("no users", u)\
            continue\
        followees = round1_follower_followee[u][0]\
        followers = round1_follower_followee[u][1]\
        for f in list(followees):\
            try:\
                all_users[int(f)]\
                g.add_edge(int(h), int(f))\
            except:\
                pass\
        for f in followers:\
            try:\
                all_users[int(f)]\
                g.add_edge(int(f), int(h))\
            except:\
                pass\
    with open("community/graph_round\{\}.pkl".format(round), "wb") as fp:\
        pickle.dump(g, fp)\
\
    coms = algorithms.hierarchical_link_community(g)\
    with open("community/coms_rb_post_round\{\}.pkl".format(round), "wb") as fp:\
        pickle.dump(coms, fp)\
}