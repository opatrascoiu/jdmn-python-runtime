#
# Copyright 2016 Goldman Sachs.
#
# Licensed under the Apache License, Version 2.0 (the "License") you may not use self file except in compliance with the License.
#
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.
#
from typing import Set, List, Union

from jdmn.runtime.annotation.Annotation import Annotation


class AnnotationSet(list):
    def addAnnotation(self, decisionName: str, ruleIndex: int, annotationName: str = None,
                      annotation: Union[str, List[str]] = None) -> None:
        # Handle case where annotationName is actually the annotation (overloaded behavior)
        if annotation is None and annotationName is not None:
            annotation = annotationName
            annotationName = None

        # Handle list annotations
        if isinstance(annotation, list):
            if annotation:  # If non-empty
                annotation = " ".join(annotation)
                self.addAnnotation(decisionName, ruleIndex, annotationName, annotation)
        elif annotation:
            # Rules index starts from 0
            if annotationName is None:
                element = Annotation(decisionName, ruleIndex + 1, annotation)
            else:
                element = Annotation(decisionName, ruleIndex + 1, annotationName + "#" + annotation)
            self.append(element)

    def toSet(self) -> Set[Annotation]:
        return set(self)
