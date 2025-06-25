import re

class BlockchainFormatter:
    """A specialized formatter for blockchain-related text"""
    
    @staticmethod
    def format_text(text):
        """Format blockchain-related text with proper spacing"""
        if not text:
            return ""
        
        # First, fix specific blockchain-related terms
        formatted_text = text
        
        # Fix specific blockchain terms
        blockchain_terms = {
            "Blockchain Technology": ["BlockchainTechnology", "Blockchaintechnology", "blockchaintechnology"],
            "blockchain technology": ["blockchaintechnology"],
            "Blockchain": ["blockchain"],
            "blockchain": ["blockchain"],
            "Bitcoin network": ["Bitcoinnetwork", "bitcoinnetwork"],
            "blockchain client": ["blockchainclient"],
            "blockchain node": ["blockchainnode"],
            "blockchain network": ["blockchainnetwork"],
            "transaction processor": ["transactionprocessor"],
            "consensus process": ["consensusprocess"],
            "ledger database": ["ledgerdatabase"],
            "data and decision": ["dataanddecision"],
            "decentralized systems": ["decentralizedsystems"],
            "public blockchain": ["publicblockchain"],
            "permissioned blockchain": ["permissionedblockchain"],
            "Genesis block": ["Genesisblock"],
            "State Database": ["StateDatabase"],
            "Chain Database": ["ChainDatabase"],
            "Hyperledger Sawtooth": ["HyperledgerSawtooth"],
            "Hyperledger Fabric": ["HyperledgerFabric"]
        }
        
        # Replace blockchain terms
        for correct_term, variations in blockchain_terms.items():
            for variation in variations:
                formatted_text = formatted_text.replace(variation, correct_term)
        
        # Fix specific phrases
        formatted_text = re.sub(r'mechanismforrevolutionizing', r'mechanism for revolutionizing', formatted_text)
        formatted_text = re.sub(r'elicitaccountabilityandeliminating', r'elicit accountability and eliminating', formatted_text)
        formatted_text = re.sub(r'Sincetheblockchain', r'Since the blockchain', formatted_text)
        formatted_text = re.sub(r'thestakeholdersofvarious', r'the stakeholders of various', formatted_text)
        formatted_text = re.sub(r'businesssystems/', r'business systems/', formatted_text)
        formatted_text = re.sub(r'organizationscancollaborate', r'organizations can collaborate', formatted_text)
        formatted_text = re.sub(r'witheachother', r'with each other', formatted_text)
        formatted_text = re.sub(r'businessinvolvestransactions', r'business involves transactions', formatted_text)
        formatted_text = re.sub(r'ndinformationexchange', r' and information exchange', formatted_text)
        formatted_text = re.sub(r'amongvariousstakeholders', r'among various stakeholders', formatted_text)
        formatted_text = re.sub(r'Blockchainisa', r'Blockchain is a', formatted_text)
        formatted_text = re.sub(r'distributedsystem', r'distributed system', formatted_text)
        formatted_text = re.sub(r'wheretransactionrecords', r'where transaction records', formatted_text)
        formatted_text = re.sub(r'arebundledinblocks', r'are bundled in blocks', formatted_text)
        formatted_text = re.sub(r'andlinkedwithprevious', r'and linked with previous', formatted_text)
        formatted_text = re.sub(r'peertopeerpayment', r'peer to peer payment', formatted_text)
        formatted_text = re.sub(r'anditisanapplication', r'and it is an application', formatted_text)
        formatted_text = re.sub(r'applicationsofrelated', r'applications of related', formatted_text)
        formatted_text = re.sub(r'businessescanreadorappend', r'businesses can read or append', formatted_text)
        formatted_text = re.sub(r'transactionrecordstothe', r'transaction records to the', formatted_text)
        formatted_text = re.sub(r'Committedtransactionsareimmutable', r'Committed transactions are immutable', formatted_text)
        formatted_text = re.sub(r'becauseeachblock', r'because each block', formatted_text)
        formatted_text = re.sub(r'islinkedwithits', r'is linked with its', formatted_text)
        formatted_text = re.sub(r'previousblockbymeans', r'previous block by means', formatted_text)
        formatted_text = re.sub(r'ofhashandsignature', r'of hash and signature', formatted_text)
        formatted_text = re.sub(r'Asshownin', r'As shown in', formatted_text)
        formatted_text = re.sub(r'blockchainecosystemconsistsof', r'blockchain ecosystem consists of', formatted_text)
        formatted_text = re.sub(r'Itmaybea', r'It may be a', formatted_text)
        formatted_text = re.sub(r'nyexistingapplication', r'ny existing application', formatted_text)
        formatted_text = re.sub(r'whichpoststransaction', r'which posts transaction', formatted_text)
        formatted_text = re.sub(r'messagetoblockchain', r'message to blockchain', formatted_text)
        formatted_text = re.sub(r'nodeisa', r'node is a', formatted_text)
        formatted_text = re.sub(r'servernodethatruns', r'server node that runs', formatted_text)
        formatted_text = re.sub(r'servicesresponsiblefor', r'services responsible for', formatted_text)
        formatted_text = re.sub(r'receivingthetransaction', r'receiving the transaction', formatted_text)
        formatted_text = re.sub(r'andtransmitsthetransaction', r'and transmits the transaction', formatted_text)
        formatted_text = re.sub(r'tootherblockchainnodes', r'to other blockchain nodes', formatted_text)
        formatted_text = re.sub(r'networkisa', r'network is a', formatted_text)
        formatted_text = re.sub(r'networkoflinked', r'network of linked', formatted_text)
        formatted_text = re.sub(r'nodesusedforread', r'nodes used for read', formatted_text)
        formatted_text = re.sub(r'writetransactionsinto', r'write transactions into', formatted_text)
        formatted_text = re.sub(r'Traditionalsystemsarecentralized', r'Traditional systems are centralized', formatted_text)
        formatted_text = re.sub(r'wherealldata', r'where all data', formatted_text)
        formatted_text = re.sub(r'makingisconcentratedona', r'making is concentrated on a', formatted_text)
        formatted_text = re.sub(r'singlenodeorcluster', r'single node or cluster', formatted_text)
        formatted_text = re.sub(r'ofnodes', r'of nodes', formatted_text)
        formatted_text = re.sub(r'Thesenodesmaintain', r'These nodes maintain', formatted_text)
        formatted_text = re.sub(r'copiesoftheshared', r'copies of the shared', formatted_text)
        formatted_text = re.sub(r'databaseanddecide', r'database and decide', formatted_text)
        formatted_text = re.sub(r'amongthemselveswhich', r'among themselves which', formatted_text)
        formatted_text = re.sub(r'dataistobecommitted', r'data is to be committed', formatted_text)
        formatted_text = re.sub(r'tothedatabaseusing', r'to the database using', formatted_text)
        formatted_text = re.sub(r'consensusmechanism', r'consensus mechanism', formatted_text)
        formatted_text = re.sub(r'distributednetworkisa', r'distributed network is a', formatted_text)
        formatted_text = re.sub(r'specialcaseofdecentralized', r'special case of decentralized', formatted_text)
        formatted_text = re.sub(r'systemwhereevery', r'system where every', formatted_text)
        formatted_text = re.sub(r'singlenodeinthe', r'single node in the', formatted_text)
        formatted_text = re.sub(r'networkmaintainsthe', r'network maintains the', formatted_text)
        formatted_text = re.sub(r'shareddatabaseand', r'shared database and', formatted_text)
        formatted_text = re.sub(r'participatesinconsensus', r'participates in consensus', formatted_text)
        formatted_text = re.sub(r'todeterminewhich', r'to determine which', formatted_text)
        formatted_text = re.sub(r'dataistobecommitted', r'data is to be committed', formatted_text)
        formatted_text = re.sub(r'tothedatabase', r'to the database', formatted_text)
        formatted_text = re.sub(r'Bitcoinand', r'Bitcoin and', formatted_text)
        formatted_text = re.sub(r'Ethereumareexamples', r'Ethereum are examples', formatted_text)
        formatted_text = re.sub(r'ofpublic', r'of public', formatted_text)
        formatted_text = re.sub(r'Consortiumblockchain', r'Consortium blockchain', formatted_text)
        formatted_text = re.sub(r'operationsarecontrolled', r'operations are controlled', formatted_text)
        formatted_text = re.sub(r'bya', r'by a', formatted_text)
        formatted_text = re.sub(r'selectedsetof', r'selected set of', formatted_text)
        formatted_text = re.sub(r'participatingorganisations', r'participating organisations', formatted_text)
        formatted_text = re.sub(r'Privateandconsortium', r'Private and consortium', formatted_text)
        formatted_text = re.sub(r'blockchainarecalled', r'blockchain are called', formatted_text)
        formatted_text = re.sub(r'permissioned', r'permissioned', formatted_text)
        formatted_text = re.sub(r'Itiscalledby', r'It is called by', formatted_text)
        formatted_text = re.sub(r'processwhenthetransaction', r'process when the transaction', formatted_text)
        formatted_text = re.sub(r'commitisstarted', r'commit is started', formatted_text)
        formatted_text = re.sub(r'Consensusisa', r'Consensus is a', formatted_text)
        formatted_text = re.sub(r'proceduretoselecta', r'procedure to select a', formatted_text)
        formatted_text = re.sub(r'leadernode', r'leader node', formatted_text)
        formatted_text = re.sub(r'whichdecides', r'which decides', formatted_text)
        formatted_text = re.sub(r'whethertheblockof', r'whether the block of', formatted_text)
        formatted_text = re.sub(r'transactionsistobe', r'transactions is to be', formatted_text)
        formatted_text = re.sub(r'committedorrejected', r'committed or rejected', formatted_text)
        formatted_text = re.sub(r'Everynodeorparticipatory', r'Every node or participatory', formatted_text)
        formatted_text = re.sub(r'nodeisgivena', r'node is given a', formatted_text)
        formatted_text = re.sub(r'miningtask', r'mining task', formatted_text)
        formatted_text = re.sub(r'anda', r'and a', formatted_text)
        formatted_text = re.sub(r'nodeelectedasleader', r'node elected as leader', formatted_text)
        formatted_text = re.sub(r'completestheminingtask', r'completes the mining task', formatted_text)
        formatted_text = re.sub(r'Nodethatparticipates', r'Node that participates', formatted_text)
        formatted_text = re.sub(r'inminingprocess', r'in mining process', formatted_text)
        formatted_text = re.sub(r'requiresheavycomputing', r'requires heavy computing', formatted_text)
        formatted_text = re.sub(r'Everynodeinthe', r'Every node in the', formatted_text)
        formatted_text = re.sub(r'processselectsrandom', r'process selects random', formatted_text)
        formatted_text = re.sub(r'timeandkeeps', r'time and keeps', formatted_text)
        formatted_text = re.sub(r'Transactionisaunit', r'Transaction is a unit', formatted_text)
        formatted_text = re.sub(r'ofbusinessdatawithin', r'of business data within', formatted_text)
        formatted_text = re.sub(r'Genesisblockisthe', r'Genesis block is the', formatted_text)
        formatted_text = re.sub(r'firstblockofchain', r'first block of chain', formatted_text)
        formatted_text = re.sub(r'createdduringinstallation', r'created during installation', formatted_text)
        formatted_text = re.sub(r'andconfiguration', r'and configuration', formatted_text)
        formatted_text = re.sub(r'Inblockchain', r'In blockchain', formatted_text)
        formatted_text = re.sub(r'ablockconsistsof', r'a block consists of', formatted_text)
        formatted_text = re.sub(r'oneormoretransactions', r'one or more transactions', formatted_text)
        formatted_text = re.sub(r'anditsrespective', r'and its respective', formatted_text)
        formatted_text = re.sub(r'treeofhashes', r'tree of hashes', formatted_text)
        formatted_text = re.sub(r'Ledger/\s*Chain\s*Databaseisa', r'Ledger/Chain Database is a', formatted_text)
        formatted_text = re.sub(r'keyvaluedatabasefora', r'key value database for a', formatted_text)
        formatted_text = re.sub(r'chainofserializedblocks', r'chain of serialized blocks', formatted_text)
        formatted_text = re.sub(r'State\s*Databaseisa', r'State Database is a', formatted_text)
        formatted_text = re.sub(r'key\s*-\s*valuedatabasefor', r'key-value database for', formatted_text)
        formatted_text = re.sub(r'storingtransactionstate', r'storing transaction state', formatted_text)
        formatted_text = re.sub(r'andlinksofitsrelated', r'and links of its related', formatted_text)
        formatted_text = re.sub(r'Istherea', r'Is there a', formatted_text)
        formatted_text = re.sub(r'needtoremove', r'need to remove', formatted_text)
        formatted_text = re.sub(r'intermediariesthataddcomplexity', r'intermediaries that add complexity', formatted_text)
        formatted_text = re.sub(r'Forexamplefor', r'For example for', formatted_text)
        formatted_text = re.sub(r'Loansanction', r'Loan sanction', formatted_text)
        formatted_text = re.sub(r'theapplicants', r'the applicants', formatted_text)
        formatted_text = re.sub(r'KYC,\s*and\s*Income', r'KYC, and Income', formatted_text)
        formatted_text = re.sub(r'statusneedstobe', r'status needs to be', formatted_text)
        formatted_text = re.sub(r'Nowadaystheabove', r'Nowadays the above', formatted_text)
        formatted_text = re.sub(r'verificationsareoutsourced', r'verifications are outsourced', formatted_text)
        formatted_text = re.sub(r'tothirdpartyagencies', r'to third party agencies', formatted_text)
        formatted_text = re.sub(r'whichistimeconsuming', r'which is time consuming', formatted_text)
        formatted_text = re.sub(r'andcostly', r'and costly', formatted_text)
        formatted_text = re.sub(r'Aftertransporterdelivers', r'After transporter delivers', formatted_text)
        formatted_text = re.sub(r'goodsorfoodgrainsto', r'goods or food grains to', formatted_text)
        formatted_text = re.sub(r'Retailshop', r'Retail shop', formatted_text)
        formatted_text = re.sub(r'atransactionaboutthe', r'a transaction about the', formatted_text)
        formatted_text = re.sub(r'deliveryonblockchain', r'delivery on blockchain', formatted_text)
        formatted_text = re.sub(r'ensuresthatithas', r'ensures that it has', formatted_text)
        formatted_text = re.sub(r'beendeliveredbecause', r'been delivered because', formatted_text)
        formatted_text = re.sub(r'itisaccessibleto', r'it is accessible to', formatted_text)
        formatted_text = re.sub(r'supplier,\s*andtransporter', r'supplier, and transporter', formatted_text)
        formatted_text = re.sub(r'Someplacesweneedto', r'Some places we need to', formatted_text)
        formatted_text = re.sub(r'proofthefinancial', r'proof the financial', formatted_text)
        formatted_text = re.sub(r'transactionforgetting', r'transaction for getting', formatted_text)
        formatted_text = re.sub(r'Incometaxrelieforother', r'Income tax relief or other', formatted_text)
        formatted_text = re.sub(r'Systemwhichensuresthe', r'System which ensures the', formatted_text)
        formatted_text = re.sub(r'transactiondatacan', r'transaction data can', formatted_text)
        formatted_text = re.sub(r'tbetampered', r't be tampered', formatted_text)
        formatted_text = re.sub(r'Doesdataneedtobe', r'Does data need to be', formatted_text)
        formatted_text = re.sub(r'sharedacrossmultiple', r'shared across multiple', formatted_text)
        formatted_text = re.sub(r'Domultipleentities', r'Do multiple entities', formatted_text)
        formatted_text = re.sub(r'needtomodifythe', r'need to modify the', formatted_text)
        formatted_text = re.sub(r'Needa', r'Need a', formatted_text)
        formatted_text = re.sub(r'completetraceofwhat', r'complete trace of what', formatted_text)
        formatted_text = re.sub(r'hasbeenmodifiedand', r'has been modified and', formatted_text)
        formatted_text = re.sub(r'bywhom', r'by whom', formatted_text)
        formatted_text = re.sub(r'Comparisonbetween', r'Comparison between', formatted_text)
        formatted_text = re.sub(r'Typebasedonavailability', r'Type based on availability', formatted_text)
        formatted_text = re.sub(r'touser', r'to user', formatted_text)
        formatted_text = re.sub(r'Sectorfocus', r'Sector focus', formatted_text)
        formatted_text = re.sub(r'Proofof', r'Proof of', formatted_text)
        formatted_text = re.sub(r'Multi\s*-\s*tenancy', r'Multi-tenancy', formatted_text)
        formatted_text = re.sub(r'Languagesupport', r'Language support', formatted_text)
        formatted_text = re.sub(r'Controlpolicies', r'Control policies', formatted_text)
        formatted_text = re.sub(r'Controlpoliciesandnetwork', r'Control policies and network', formatted_text)
        formatted_text = re.sub(r'Needtoencryptthe', r'Need to encrypt the', formatted_text)
        formatted_text = re.sub(r'Scalable,\s*Performance', r'Scalable, Performance', formatted_text)
        formatted_text = re.sub(r'dependsonconsensus', r'depends on consensus', formatted_text)
        formatted_text = re.sub(r'algorithmand', r'algorithm and', formatted_text)
        formatted_text = re.sub(r'ndnumberofnodes', r'nd number of nodes', formatted_text)
        formatted_text = re.sub(r'blocksizeandcompute', r'block size and compute', formatted_text)
        formatted_text = re.sub(r'Projecttypeand', r'Project type and', formatted_text)
        formatted_text = re.sub(r'maintainer', r'maintainer', formatted_text)
        formatted_text = re.sub(r'Opensourceand', r'Open source and', formatted_text)
        formatted_text = re.sub(r'maintainedby', r'maintained by', formatted_text)
        formatted_text = re.sub(r'Whileselectingthe', r'While selecting the', formatted_text)
        formatted_text = re.sub(r'sectorforadopting', r'sector for adopting', formatted_text)
        formatted_text = re.sub(r'essentialcareneedsto', r'essential care needs to', formatted_text)
        formatted_text = re.sub(r'takentoassessits', r'taken to assess its', formatted_text)
        formatted_text = re.sub(r'suitabilityforthesector', r'suitability for the sector', formatted_text)
        formatted_text = re.sub(r'Identifyingthebest', r'Identifying the best', formatted_text)
        formatted_text = re.sub(r'platformfordifferent', r'platform for different', formatted_text)
        formatted_text = re.sub(r'classesofapplication', r'classes of application', formatted_text)
        formatted_text = re.sub(r'requiresdetailedstudy', r'requires detailed study', formatted_text)
        formatted_text = re.sub(r'andevaluation', r'and evaluation', formatted_text)
        
        # Fix spacing between sentences
        formatted_text = re.sub(r'\.([A-Z])', r'. \1', formatted_text)
        
        # Fix spacing after commas
        formatted_text = re.sub(r',([A-Za-z])', r', \1', formatted_text)
        
        # Remove excessive whitespace
        formatted_text = re.sub(r'\s{2,}', ' ', formatted_text)
        
        return formatted_text.strip()
    
    @staticmethod
    def format_blockchain_keywords(keywords):
        """Format blockchain-related keywords"""
        formatted_keywords = []
        
        for keyword in keywords:
            term = keyword["term"]
            score = keyword["score"]
            
            # Format the term
            formatted_term = BlockchainFormatter.format_text(term)
            
            # Add to formatted keywords
            formatted_keywords.append({
                "term": formatted_term,
                "score": score
            })
        
        return formatted_keywords