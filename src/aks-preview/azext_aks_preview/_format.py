# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from collections import OrderedDict
# pylint: disable=import-error
from jmespath import compile as compile_jmes, Options
# pylint: disable=import-error
from jmespath import functions


def aks_addon_list_available_table_format(result):
    def parser(entry):
        parsed = compile_jmes("""{
                name: name,
                description: description
            }""")
        return parsed.search(entry, Options(dict_cls=OrderedDict))
    return [parser(r) for r in result]


def aks_addon_list_table_format(result):
    def parser(entry):
        parsed = compile_jmes("""{
                name: name,
                enabled: enabled
            }""")
        return parsed.search(entry, Options(dict_cls=OrderedDict))
    return [parser(r) for r in result]


def aks_addon_show_table_format(result):
    def parser(entry):
        config = ""
        for k, v in entry["config"].items():
            config += k + "=" + v + ";"
        entry["config"] = config
        parsed = compile_jmes("""{
                name: name,
                api_key: api_key,
                config: config,
                identity: identity
            }""")
        return parsed.search(entry, Options(dict_cls=OrderedDict))
    return parser(result)


def aks_agentpool_show_table_format(result):
    """Format an agent pool as summary results for display with "-o table"."""
    return [_aks_agentpool_table_format(result)]


def _aks_agentpool_table_format(result):
    parsed = compile_jmes("""{
        name: name,
        osType: osType,
        kubernetesVersion: kubernetesVersion,
        vmSize: vmSize,
        osDiskSizeGB: osDiskSizeGB,
        count: count,
        maxPods: maxPods,
        provisioningState: provisioningState,
        mode: mode
    }""")
    # use ordered dicts so headers are predictable
    return parsed.search(result, Options(dict_cls=OrderedDict))


def aks_agentpool_list_table_format(results):
    """Format an agent pool list for display with "-o table"."""
    return [_aks_agentpool_table_format(r) for r in results]


def aks_list_table_format(results):
    """"Format a list of managed clusters as summary results for display with "-o table"."""
    return [_aks_table_format(r) for r in results]


def aks_show_table_format(result):
    """Format a managed cluster as summary results for display with "-o table"."""
    return [_aks_table_format(result)]


def _aks_table_format(result):
    parsed = compile_jmes("""{
        name: name,
        location: location,
        resourceGroup: resourceGroup,
        kubernetesVersion: kubernetesVersion,
        provisioningState: provisioningState,
        fqdn: fqdn
    }""")
    # use ordered dicts so headers are predictable
    return parsed.search(result, Options(dict_cls=OrderedDict))


def aks_upgrades_table_format(result):
    """Format get-upgrades results as a summary for display with "-o table"."""

    preview = {}

    def find_preview_versions(versions_bag):
        for upgrade in versions_bag.get('upgrades', []):
            if upgrade.get('isPreview', False):
                preview[upgrade['kubernetesVersion']] = True
    find_preview_versions(result.get('controlPlaneProfile', {}))

    # This expression assumes there is one node pool, and that the master and nodes upgrade in lockstep.
    parsed = compile_jmes("""{
        name: name,
        resourceGroup: resourceGroup,
        masterVersion: controlPlaneProfile.kubernetesVersion || `unknown`,
        upgrades: controlPlaneProfile.upgrades[].kubernetesVersion || [`None available`] | sort_versions(@) | set_preview_array(@) | join(`, `, @)
    }""")
    # use ordered dicts so headers are predictable
    return parsed.search(result, Options(dict_cls=OrderedDict, custom_functions=_custom_functions(preview)))


def aks_versions_table_format(result):
    """Format get-versions results as a summary for display with "-o table"."""

    # get preview orchestrator version
    preview = {}

    def find_preview_versions():
        for orchestrator in result.get('orchestrators', []):
            if orchestrator.get('isPreview', False):
                preview[orchestrator['orchestratorVersion']] = True
    find_preview_versions()

    parsed = compile_jmes("""orchestrators[].{
        kubernetesVersion: orchestratorVersion | set_preview(@),
        upgrades: upgrades[].orchestratorVersion || [`None available`] | sort_versions(@) | set_preview_array(@) | join(`, `, @)
    }""")
    # use ordered dicts so headers are predictable
    results = parsed.search(result, Options(
        dict_cls=OrderedDict, custom_functions=_custom_functions(preview)))
    return sorted(results, key=lambda x: version_to_tuple(x.get('kubernetesVersion')), reverse=True)


def version_to_tuple(version):
    """Removes preview suffix"""
    if version.endswith('(preview)'):
        version = version[:-len('(preview)')]
    return tuple(map(int, (version.split('.'))))


def _custom_functions(preview_versions):
    class CustomFunctions(functions.Functions):  # pylint: disable=too-few-public-methods

        @ functions.signature({'types': ['array']})
        def _func_sort_versions(self, versions):  # pylint: disable=no-self-use
            """Custom JMESPath `sort_versions` function that sorts an array of strings as software versions"""
            try:
                return sorted(versions, key=version_to_tuple)
            # if it wasn't sortable, return the input so the pipeline continues
            except (TypeError, ValueError):
                return versions

        @ functions.signature({'types': ['array']})
        def _func_set_preview_array(self, versions):
            """Custom JMESPath `set_preview_array` function that suffixes preview version"""
            try:
                for i, _ in enumerate(versions):
                    versions[i] = self._func_set_preview(versions[i])
                return versions
            except(TypeError, ValueError):
                return versions

        @ functions.signature({'types': ['string']})
        def _func_set_preview(self, version):  # pylint: disable=no-self-use
            """Custom JMESPath `set_preview` function that suffixes preview version"""
            try:
                if preview_versions.get(version, False):
                    return version + '(preview)'
                return version
            except(TypeError, ValueError):
                return version

        @ functions.signature({'types': ['object']})
        def _func_pprint_labels(self, labels):  # pylint: disable=no-self-use
            """Custom JMESPath `pprint_labels` function that pretty print labels"""
            if not labels:
                return ''
            return ' '.join([
                '{}={}'.format(k, labels[k])
                for k in sorted(labels.keys())
            ])

    return CustomFunctions()


def aks_pod_identity_exceptions_table_format(result):
    """Format pod identity exceptions results as a summary for display with "-o table"."""
    preview = {}
    parsed = compile_jmes("""podIdentityProfile.userAssignedIdentityExceptions[].{
        name: name,
        namespace: namespace,
        PodLabels: podLabels | pprint_labels(@)
    }""")
    # use ordered dicts so headers are predictable
    return parsed.search(result, Options(dict_cls=OrderedDict, custom_functions=_custom_functions(preview)))


def aks_pod_identities_table_format(result):
    """Format pod identities results as a summary for display with "-o table"."""
    preview = {}
    parsed = compile_jmes("""podIdentityProfile.userAssignedIdentities[].{
        name: name,
        namespace: namespace,
        provisioningState: provisioningState
        identity: identity.resourceId
    }""")
    # use ordered dicts so headers are predictable
    return parsed.search(result, Options(dict_cls=OrderedDict, custom_functions=_custom_functions(preview)))
