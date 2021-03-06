#
import FWCore.ParameterSet.Config as cms

process = cms.Process("i")


process.MessageLogger = cms.Service("MessageLogger",
     debugModules = cms.untracked.vstring('dumper'),
     destinations = cms.untracked.vstring('cout'),
#    destinations = cms.untracked.vstring("log","cout"),
     cout = cms.untracked.PSet(
#         threshold = cms.untracked.string('DEBUG')
         threshold = cms.untracked.string('WARNING')
     )
#    log = cms.untracked.PSet(
#        threshold = cms.untracked.string('DEBUG')
#    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


process.source = cms.Source("PoolSource",
#    fileNames = cms.untracked.vstring('file:/afs/cern.ch/work/d/dkotlins/public/digis.root'))
    fileNames = cms.untracked.vstring('file:../scripts/digis.root'))

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('fed_errors.root')
)

process.dumper = cms.EDAnalyzer("PixelFedErrorDumper", 
    Verbosity = cms.untracked.bool(True),
    InputLabel = cms.untracked.string('siPixelDigis'),
)

process.p = cms.Path(process.dumper)


