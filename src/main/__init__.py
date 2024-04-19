"""An example of using another module from different in SDK
"""

import dagger
from dagger import dag, function, object_type


@object_type
class Bar:
    @function
    async def go_build(self, source: dagger.Directory) -> dagger.Container:
        """Builds and containerizes my go app"""
        return dag.foo().build(source)

    @function
    async def run(self, source: dagger.Directory) -> str:
        """Emits stdout of my go app container"""
        return await self.go_build(source).stdout()
