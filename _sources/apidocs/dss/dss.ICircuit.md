# {py:mod}`dss.ICircuit`

```{py:module} dss.ICircuit
```

```{autodoc2-docstring} dss.ICircuit
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ICircuit <dss.ICircuit.ICircuit>`
  - ```{autodoc2-docstring} dss.ICircuit.ICircuit
    :summary:
    ```
````

### API

`````{py:class} ICircuit(api_util)
:canonical: dss.ICircuit.ICircuit

Bases: {py:obj}`dss._cffi_api_util.Base`

```{autodoc2-docstring} dss.ICircuit.ICircuit
```

````{py:attribute} ActiveBus
:canonical: dss.ICircuit.ICircuit.ActiveBus
:type: dss.IBus.IBus
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.ActiveBus
```

````

````{py:attribute} ActiveCktElement
:canonical: dss.ICircuit.ICircuit.ActiveCktElement
:type: dss.ICktElement.ICktElement
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.ActiveCktElement
```

````

````{py:attribute} ActiveClass
:canonical: dss.ICircuit.ICircuit.ActiveClass
:type: dss.IActiveClass.IActiveClass
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.ActiveClass
```

````

````{py:attribute} ActiveDSSElement
:canonical: dss.ICircuit.ICircuit.ActiveDSSElement
:type: dss.IDSSElement.IDSSElement
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.ActiveDSSElement
```

````

````{py:attribute} ActiveElement
:canonical: dss.ICircuit.ICircuit.ActiveElement
:type: dss.ICktElement.ICktElement
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.ActiveElement
```

````

````{py:property} AllBusDistances
:canonical: dss.ICircuit.ICircuit.AllBusDistances
:type: dss._types.Float64Array

```{autodoc2-docstring} dss.ICircuit.ICircuit.AllBusDistances
```

````

````{py:property} AllBusNames
:canonical: dss.ICircuit.ICircuit.AllBusNames
:type: typing.List[str]

```{autodoc2-docstring} dss.ICircuit.ICircuit.AllBusNames
```

````

````{py:property} AllBusVmag
:canonical: dss.ICircuit.ICircuit.AllBusVmag
:type: dss._types.Float64Array

```{autodoc2-docstring} dss.ICircuit.ICircuit.AllBusVmag
```

````

````{py:property} AllBusVmagPu
:canonical: dss.ICircuit.ICircuit.AllBusVmagPu
:type: dss._types.Float64Array

```{autodoc2-docstring} dss.ICircuit.ICircuit.AllBusVmagPu
```

````

````{py:property} AllBusVolts
:canonical: dss.ICircuit.ICircuit.AllBusVolts
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.ICircuit.ICircuit.AllBusVolts
```

````

````{py:property} AllElementLosses
:canonical: dss.ICircuit.ICircuit.AllElementLosses
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.ICircuit.ICircuit.AllElementLosses
```

````

````{py:property} AllElementNames
:canonical: dss.ICircuit.ICircuit.AllElementNames
:type: typing.List[str]

```{autodoc2-docstring} dss.ICircuit.ICircuit.AllElementNames
```

````

````{py:property} AllNodeDistances
:canonical: dss.ICircuit.ICircuit.AllNodeDistances
:type: dss._types.Float64Array

```{autodoc2-docstring} dss.ICircuit.ICircuit.AllNodeDistances
```

````

````{py:method} AllNodeDistancesByPhase(Phase: int) -> dss._types.Float64Array
:canonical: dss.ICircuit.ICircuit.AllNodeDistancesByPhase

```{autodoc2-docstring} dss.ICircuit.ICircuit.AllNodeDistancesByPhase
```

````

````{py:property} AllNodeNames
:canonical: dss.ICircuit.ICircuit.AllNodeNames
:type: typing.List[str]

```{autodoc2-docstring} dss.ICircuit.ICircuit.AllNodeNames
```

````

````{py:method} AllNodeNamesByPhase(Phase: int) -> typing.List[str]
:canonical: dss.ICircuit.ICircuit.AllNodeNamesByPhase

```{autodoc2-docstring} dss.ICircuit.ICircuit.AllNodeNamesByPhase
```

````

````{py:method} AllNodeVmagByPhase(Phase: int) -> dss._types.Float64Array
:canonical: dss.ICircuit.ICircuit.AllNodeVmagByPhase

```{autodoc2-docstring} dss.ICircuit.ICircuit.AllNodeVmagByPhase
```

````

````{py:method} AllNodeVmagPUByPhase(Phase: int) -> dss._types.Float64Array
:canonical: dss.ICircuit.ICircuit.AllNodeVmagPUByPhase

```{autodoc2-docstring} dss.ICircuit.ICircuit.AllNodeVmagPUByPhase
```

````

````{py:attribute} Buses
:canonical: dss.ICircuit.ICircuit.Buses
:type: dss.IBus.IBus
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.Buses
```

````

````{py:attribute} CNData
:canonical: dss.ICircuit.ICircuit.CNData
:type: dss.ICNData.ICNData
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.CNData
```

````

````{py:attribute} CapControls
:canonical: dss.ICircuit.ICircuit.CapControls
:type: dss.ICapControls.ICapControls
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.CapControls
```

````

````{py:attribute} Capacitors
:canonical: dss.ICircuit.ICircuit.Capacitors
:type: dss.ICapacitors.ICapacitors
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.Capacitors
```

````

````{py:method} Capacity(Start: float, Increment: float) -> float
:canonical: dss.ICircuit.ICircuit.Capacity

```{autodoc2-docstring} dss.ICircuit.ICircuit.Capacity
```

````

````{py:attribute} CktElements
:canonical: dss.ICircuit.ICircuit.CktElements
:type: dss.ICktElement.ICktElement
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.CktElements
```

````

````{py:attribute} CtrlQueue
:canonical: dss.ICircuit.ICircuit.CtrlQueue
:type: dss.ICtrlQueue.ICtrlQueue
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.CtrlQueue
```

````

````{py:attribute} DSSim_Coms
:canonical: dss.ICircuit.ICircuit.DSSim_Coms
:type: dss.IDSSimComs.IDSSimComs
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.DSSim_Coms
```

````

````{py:method} Disable(Name: typing.AnyStr)
:canonical: dss.ICircuit.ICircuit.Disable

```{autodoc2-docstring} dss.ICircuit.ICircuit.Disable
```

````

````{py:method} ElementLosses(Value: dss._types.Int32Array) -> dss._types.Float64ArrayOrComplexArray
:canonical: dss.ICircuit.ICircuit.ElementLosses

```{autodoc2-docstring} dss.ICircuit.ICircuit.ElementLosses
```

````

````{py:method} Enable(Name: typing.AnyStr)
:canonical: dss.ICircuit.ICircuit.Enable

```{autodoc2-docstring} dss.ICircuit.ICircuit.Enable
```

````

````{py:method} EndOfTimeStepUpdate()
:canonical: dss.ICircuit.ICircuit.EndOfTimeStepUpdate

```{autodoc2-docstring} dss.ICircuit.ICircuit.EndOfTimeStepUpdate
```

````

````{py:method} FirstElement() -> int
:canonical: dss.ICircuit.ICircuit.FirstElement

```{autodoc2-docstring} dss.ICircuit.ICircuit.FirstElement
```

````

````{py:method} FirstPCElement() -> int
:canonical: dss.ICircuit.ICircuit.FirstPCElement

```{autodoc2-docstring} dss.ICircuit.ICircuit.FirstPCElement
```

````

````{py:method} FirstPDElement() -> int
:canonical: dss.ICircuit.ICircuit.FirstPDElement

```{autodoc2-docstring} dss.ICircuit.ICircuit.FirstPDElement
```

````

````{py:method} FromJSON(data: typing.Union[typing.AnyStr, dict], options: dss.enums.DSSJSONFlags = 0)
:canonical: dss.ICircuit.ICircuit.FromJSON

```{autodoc2-docstring} dss.ICircuit.ICircuit.FromJSON
```

````

````{py:attribute} Fuses
:canonical: dss.ICircuit.ICircuit.Fuses
:type: dss.IFuses.IFuses
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.Fuses
```

````

````{py:attribute} GICSources
:canonical: dss.ICircuit.ICircuit.GICSources
:type: dss.IGICSources.IGICSources
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.GICSources
```

````

````{py:attribute} Generators
:canonical: dss.ICircuit.ICircuit.Generators
:type: dss.IGenerators.IGenerators
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.Generators
```

````

````{py:attribute} ISources
:canonical: dss.ICircuit.ICircuit.ISources
:type: dss.IISources.IISources
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.ISources
```

````

````{py:attribute} Isources
:canonical: dss.ICircuit.ICircuit.Isources
:type: dss.IISources.IISources
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.Isources
```

````

````{py:attribute} LineCodes
:canonical: dss.ICircuit.ICircuit.LineCodes
:type: dss.ILineCodes.ILineCodes
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.LineCodes
```

````

````{py:attribute} LineGeometries
:canonical: dss.ICircuit.ICircuit.LineGeometries
:type: dss.ILineGeometries.ILineGeometries
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.LineGeometries
```

````

````{py:property} LineLosses
:canonical: dss.ICircuit.ICircuit.LineLosses
:type: dss._types.Float64ArrayOrSimpleComplex

```{autodoc2-docstring} dss.ICircuit.ICircuit.LineLosses
```

````

````{py:attribute} LineSpacings
:canonical: dss.ICircuit.ICircuit.LineSpacings
:type: dss.ILineSpacings.ILineSpacings
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.LineSpacings
```

````

````{py:attribute} Lines
:canonical: dss.ICircuit.ICircuit.Lines
:type: dss.ILines.ILines
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.Lines
```

````

````{py:attribute} LoadShapes
:canonical: dss.ICircuit.ICircuit.LoadShapes
:type: dss.ILoadShapes.ILoadShapes
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.LoadShapes
```

````

````{py:attribute} Loads
:canonical: dss.ICircuit.ICircuit.Loads
:type: dss.ILoads.ILoads
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.Loads
```

````

````{py:property} Losses
:canonical: dss.ICircuit.ICircuit.Losses
:type: dss._types.Float64ArrayOrSimpleComplex

```{autodoc2-docstring} dss.ICircuit.ICircuit.Losses
```

````

````{py:attribute} Meters
:canonical: dss.ICircuit.ICircuit.Meters
:type: dss.IMeters.IMeters
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.Meters
```

````

````{py:attribute} Monitors
:canonical: dss.ICircuit.ICircuit.Monitors
:type: dss.IMonitors.IMonitors
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.Monitors
```

````

````{py:property} Name
:canonical: dss.ICircuit.ICircuit.Name
:type: str

```{autodoc2-docstring} dss.ICircuit.ICircuit.Name
```

````

````{py:method} NextElement() -> int
:canonical: dss.ICircuit.ICircuit.NextElement

```{autodoc2-docstring} dss.ICircuit.ICircuit.NextElement
```

````

````{py:method} NextPCElement() -> int
:canonical: dss.ICircuit.ICircuit.NextPCElement

```{autodoc2-docstring} dss.ICircuit.ICircuit.NextPCElement
```

````

````{py:method} NextPDElement() -> int
:canonical: dss.ICircuit.ICircuit.NextPDElement

```{autodoc2-docstring} dss.ICircuit.ICircuit.NextPDElement
```

````

````{py:property} NumBuses
:canonical: dss.ICircuit.ICircuit.NumBuses
:type: int

```{autodoc2-docstring} dss.ICircuit.ICircuit.NumBuses
```

````

````{py:property} NumCktElements
:canonical: dss.ICircuit.ICircuit.NumCktElements
:type: int

```{autodoc2-docstring} dss.ICircuit.ICircuit.NumCktElements
```

````

````{py:property} NumNodes
:canonical: dss.ICircuit.ICircuit.NumNodes
:type: int

```{autodoc2-docstring} dss.ICircuit.ICircuit.NumNodes
```

````

````{py:attribute} PDElements
:canonical: dss.ICircuit.ICircuit.PDElements
:type: dss.IPDElements.IPDElements
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.PDElements
```

````

````{py:attribute} PVSystems
:canonical: dss.ICircuit.ICircuit.PVSystems
:type: dss.IPVSystems.IPVSystems
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.PVSystems
```

````

````{py:attribute} Parallel
:canonical: dss.ICircuit.ICircuit.Parallel
:type: dss.IParallel.IParallel
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.Parallel
```

````

````{py:property} ParentPDElement
:canonical: dss.ICircuit.ICircuit.ParentPDElement
:type: int

```{autodoc2-docstring} dss.ICircuit.ICircuit.ParentPDElement
```

````

````{py:attribute} Reactors
:canonical: dss.ICircuit.ICircuit.Reactors
:type: dss.IReactors.IReactors
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.Reactors
```

````

````{py:attribute} Reclosers
:canonical: dss.ICircuit.ICircuit.Reclosers
:type: dss.IReclosers.IReclosers
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.Reclosers
```

````

````{py:attribute} ReduceCkt
:canonical: dss.ICircuit.ICircuit.ReduceCkt
:type: dss.IReduceCkt.IReduceCkt
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.ReduceCkt
```

````

````{py:attribute} RegControls
:canonical: dss.ICircuit.ICircuit.RegControls
:type: dss.IRegControls.IRegControls
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.RegControls
```

````

````{py:attribute} Relays
:canonical: dss.ICircuit.ICircuit.Relays
:type: dss.IRelays.IRelays
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.Relays
```

````

````{py:method} Sample()
:canonical: dss.ICircuit.ICircuit.Sample

```{autodoc2-docstring} dss.ICircuit.ICircuit.Sample
```

````

````{py:method} Save(dirOrFilePath: typing.AnyStr, options: dss.enums.DSSSaveFlags) -> str
:canonical: dss.ICircuit.ICircuit.Save

```{autodoc2-docstring} dss.ICircuit.ICircuit.Save
```

````

````{py:method} SaveSample()
:canonical: dss.ICircuit.ICircuit.SaveSample

```{autodoc2-docstring} dss.ICircuit.ICircuit.SaveSample
```

````

````{py:attribute} Sensors
:canonical: dss.ICircuit.ICircuit.Sensors
:type: dss.ISensors.ISensors
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.Sensors
```

````

````{py:method} SetActiveBus(BusName: typing.AnyStr) -> int
:canonical: dss.ICircuit.ICircuit.SetActiveBus

```{autodoc2-docstring} dss.ICircuit.ICircuit.SetActiveBus
```

````

````{py:method} SetActiveBusi(BusIndex: int) -> int
:canonical: dss.ICircuit.ICircuit.SetActiveBusi

```{autodoc2-docstring} dss.ICircuit.ICircuit.SetActiveBusi
```

````

````{py:method} SetActiveClass(ClassName: typing.AnyStr) -> int
:canonical: dss.ICircuit.ICircuit.SetActiveClass

```{autodoc2-docstring} dss.ICircuit.ICircuit.SetActiveClass
```

````

````{py:method} SetActiveElement(FullName: typing.AnyStr) -> int
:canonical: dss.ICircuit.ICircuit.SetActiveElement

```{autodoc2-docstring} dss.ICircuit.ICircuit.SetActiveElement
```

````

````{py:attribute} Settings
:canonical: dss.ICircuit.ICircuit.Settings
:type: dss.ISettings.ISettings
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.Settings
```

````

````{py:attribute} Solution
:canonical: dss.ICircuit.ICircuit.Solution
:type: dss.ISolution.ISolution
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.Solution
```

````

````{py:attribute} Storages
:canonical: dss.ICircuit.ICircuit.Storages
:type: dss.IStorages.IStorages
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.Storages
```

````

````{py:property} SubstationLosses
:canonical: dss.ICircuit.ICircuit.SubstationLosses
:type: dss._types.Float64ArrayOrSimpleComplex

```{autodoc2-docstring} dss.ICircuit.ICircuit.SubstationLosses
```

````

````{py:attribute} SwtControls
:canonical: dss.ICircuit.ICircuit.SwtControls
:type: dss.ISwtControls.ISwtControls
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.SwtControls
```

````

````{py:property} SystemY
:canonical: dss.ICircuit.ICircuit.SystemY
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.ICircuit.ICircuit.SystemY
```

````

````{py:attribute} TSData
:canonical: dss.ICircuit.ICircuit.TSData
:type: dss.ITSData.ITSData
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.TSData
```

````

````{py:method} ToJSON(options: dss.enums.DSSJSONFlags = 0) -> str
:canonical: dss.ICircuit.ICircuit.ToJSON

```{autodoc2-docstring} dss.ICircuit.ICircuit.ToJSON
```

````

````{py:attribute} Topology
:canonical: dss.ICircuit.ICircuit.Topology
:type: dss.ITopology.ITopology
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.Topology
```

````

````{py:property} TotalPower
:canonical: dss.ICircuit.ICircuit.TotalPower
:type: dss._types.Float64ArrayOrSimpleComplex

```{autodoc2-docstring} dss.ICircuit.ICircuit.TotalPower
```

````

````{py:attribute} Transformers
:canonical: dss.ICircuit.ICircuit.Transformers
:type: dss.ITransformers.ITransformers
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.Transformers
```

````

````{py:method} UpdateStorage()
:canonical: dss.ICircuit.ICircuit.UpdateStorage

```{autodoc2-docstring} dss.ICircuit.ICircuit.UpdateStorage
```

````

````{py:attribute} Vsources
:canonical: dss.ICircuit.ICircuit.Vsources
:type: dss.IVsources.IVsources
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.Vsources
```

````

````{py:attribute} WireData
:canonical: dss.ICircuit.ICircuit.WireData
:type: dss.IWireData.IWireData
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.WireData
```

````

````{py:attribute} XYCurves
:canonical: dss.ICircuit.ICircuit.XYCurves
:type: dss.IXYCurves.IXYCurves
:value: >
   None

```{autodoc2-docstring} dss.ICircuit.ICircuit.XYCurves
```

````

````{py:property} YCurrents
:canonical: dss.ICircuit.ICircuit.YCurrents
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.ICircuit.ICircuit.YCurrents
```

````

````{py:property} YNodeOrder
:canonical: dss.ICircuit.ICircuit.YNodeOrder
:type: typing.List[str]

```{autodoc2-docstring} dss.ICircuit.ICircuit.YNodeOrder
```

````

````{py:property} YNodeVarray
:canonical: dss.ICircuit.ICircuit.YNodeVarray
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.ICircuit.ICircuit.YNodeVarray
```

````

````{py:method} __init__(api_util)
:canonical: dss.ICircuit.ICircuit.__init__

```{autodoc2-docstring} dss.ICircuit.ICircuit.__init__
```

````

`````
