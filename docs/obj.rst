DSS.Obj
=======

This represents a work-in-progress effort to expose all OpenDSS data classes to the end user without requiring
frequent string manipulation. All data is available using native Python types and wrapper objects.

A new batch API is also integrated, allowing easy manipulation of multiple objects of the same type in a consistent
manner.

Changes are expected to adjust naming of the properties. New features are also planned.

.. automodule:: dss.IObj

   .. rubric:: Classes

   .. autosummary::
   
      AutoAddDeviceType
      AutoTrans
      AutoTransBatch
      BatchFloat64ArrayProxy
      BatchInt32ArrayProxy
      CNData
      CNDataBatch
      CapControl
      CapControlBatch
      Capacitor
      CapacitorBatch
      CircuitModel
      Connection
      ControlMode
      CoreType
      DSSBatch
      DSSObj
      DimensionUnits
      ESPVLControl
      ESPVLControlBatch
      EarthModel
      EnergyMeter
      EnergyMeterBatch
      ExpControl
      ExpControlBatch
      Fault
      FaultBatch
      Fuse
      FuseBatch
      GICLine
      GICLineBatch
      GICTransformer
      GICTransformerBatch
      GICsource
      GICsourceBatch
      GenDispatcher
      GenDispatcherBatch
      Generator
      GeneratorBatch
      GrowthShape
      GrowthShapeBatch
      IDSSObj
      IObj
      IndMach012
      IndMach012Batch
      InvControl
      InvControlBatch
      Isource
      IsourceBatch
      Line
      LineBatch
      LineCode
      LineCodeBatch
      LineGeometry
      LineGeometryBatch
      LineSpacing
      LineSpacingBatch
      LineType
      Load
      LoadBatch
      LoadShape
      LoadShapeBatch
      LoadShapeClass
      LoadSolutionModel
      Monitor
      MonitorBatch
      MonitoredPhase
      PVSystem
      PVSystemBatch
      PhaseSequence
      PriceShape
      PriceShapeBatch
      RandomType
      Reactor
      ReactorBatch
      Recloser
      RecloserBatch
      RegControl
      RegControlBatch
      Relay
      RelayBatch
      ScanType
      Sensor
      SensorBatch
      SequenceType
      SolutionAlgorithm
      SolutionMode
      Spectrum
      SpectrumBatch
      Storage
      StorageBatch
      StorageController
      StorageControllerBatch
      SwtControl
      SwtControlBatch
      TCC_Curve
      TCC_CurveBatch
      TSData
      TSDataBatch
      TShape
      TShapeBatch
      Transformer
      TransformerBatch
      UPFC
      UPFCBatch
      UPFCControl
      UPFCControlBatch
      VCCS
      VCCSBatch
      VSConverter
      VSConverterBatch
      Vsource
      VsourceBatch
      WireData
      WireDataBatch
      XYcurve
      XYcurveBatch
      XfmrCode
      XfmrCodeBatch
