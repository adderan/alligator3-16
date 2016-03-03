#!/bin/sh

ROOT_DIR=$(readlink -f "$(dirname "$0")")
CACTUS_DIR=$ROOT_DIR/progressiveCactus_alligator1603
CACTUS_CONFIG=$ROOT_DIR/cactus_progressive_config_alligator_1603.xml
SEQ_FILE=$ROOT_DIR/alligator_1603_seqFile.txt
PROGRESSIVE_CACTUS_VERSION=0959ae8017a3dc85e93ba60673c7bad1b33c5d14


if [ ! -f $CACTUS_DIR ]; then
    git clone https://github.com/glennhickey/progressiveCactus $CACTUS_DIR
fi


cd $CACTUS_DIR && git checkout $PROGRESSIVE_CACTUS_VERSION && git submodule update --init && make


$CACTUS_DIR/bin/runProgressiveCactus.sh $SEQ_FILE $ROOT_DIR/work $ROOT_DIR/alligator_1603_alignment.hal --stats --configFile $CACTUS_CONFIG --batchSystem parasol --parasolCommand "/cluster/home/adderan/local/bin/parasol -host=ku" --bigBatchSystem singleMachine --defaultMemory 8589934593 --bigMemoryThreshold 8589934592 --bigMaxMemory 893353197568 --bigMaxCpus 30 --maxThreads 30 --retryCount 3