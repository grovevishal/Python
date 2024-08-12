import asyncio
from pysnmp.hlapi.asyncio import *
from pysnmp.smi.rfc1902 import ObjectIdentity, ObjectType

async def get_snmp_data():
    snmp_engine = SnmpEngine()
    errorIndication, errorStatus, errorIndex, varBinds = await getCmd(
        snmp_engine,
        CommunityData('public'),
        UdpTransportTarget(('127.0.0.1', 161)),
        ContextData(),
        ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysContact', 0)),ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysName', 0)),ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysLocation', 0)),ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysServices', 0))
    )

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print(
            f"{errorStatus.prettyPrint()} at {errorIndex and varBinds[int(errorIndex) - 1][0] or '?'}"
        )
    else:
        # print(varBinds)
        for varBind in varBinds:
           print(varBind[1])
        # for varBind in varBinds:
        #     print(None)
        #     # print(" = ".join([x.prettyPrint() for x in varBind]))

async def main():
    await get_snmp_data()

asyncio.run(main())
