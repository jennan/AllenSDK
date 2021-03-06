# Copyright 2016 Allen Institute for Brain Science
# This file is part of Allen SDK.
#
# Allen SDK is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# Allen SDK is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# Merchantability Or Fitness FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Allen SDK.  If not, see <http://www.gnu.org/licenses/>.

import pytest
from mock import MagicMock
from allensdk.api.queries.image_download_api import ImageDownloadApi


@pytest.fixture
def image_api():
    image_api = ImageDownloadApi()

    image_api.retrieve_file_over_http = \
        MagicMock(name='retrieve_file_over_http')
    image_api.json_msg_query = MagicMock(name='json_msg_query')

    return image_api


def test_api_doc_url_download_section_image_downsampled(image_api):
    '''
    Notes
    -----
    See: `Experimental Overview and Metadata `<http://help.brain-map.org/display/mouseconnectivity/API#API-ExperimentalOverviewandMetadata>_
    , link labeled 'Download image downsampled by factor of 6 using default thresholds'.
    '''
    path = '126862575.jpg'

    section_image_id = 126862575
    image_api.download_section_image(section_image_id,
                                     downsample=6,
                                     range=[0, 932, 0, 1279, 0, 4095])

    image_api.retrieve_file_over_http.assert_called_once_with(
        "http://api.brain-map.org/api/v2/section_image_download/126862575"
        "?downsample=6&range=0,932,0,1279,0,4095",
        path)


def test_api_doc_url_download_section_image_downsample_dimensions(image_api):
    path = '126862575.jpg'

    section_image_id = 126862575
    image_api.download_section_image(section_image_id,
                                     downsample=6,
                                     downsample_dimensions=True)

    image_api.retrieve_file_over_http.assert_called_once_with(
        "http://api.brain-map.org/api/v2/section_image_download/126862575"
        "?downsample=6&downsample_dimensions=true",
        path)


def test_api_doc_url_download_section_image_full_res(image_api):
    path = '126862575.jpg'

    section_image_id = 126862575
    image_api.download_section_image(section_image_id)

    image_api.retrieve_file_over_http.assert_called_once_with(
        "http://api.brain-map.org/api/v2/section_image_download/126862575",
        path)


def test_api_doc_url_download_section_image_downsample_dimensions_false(image_api):
    path = '126862575.jpg'

    section_image_id = 126862575
    image_api.download_section_image(section_image_id,
                                     downsample=6,
                                     downsample_dimensions=False)

    image_api.retrieve_file_over_http.assert_called_once_with(
        "http://api.brain-map.org/api/v2/section_image_download/126862575"
        "?downsample=6&downsample_dimensions=false",
        path)


def test_api_doc_url_download_section_image_downsampled_low_quality(image_api):
    path = '126862575.jpg'

    section_image_id = 126862575
    image_api.download_section_image(section_image_id,
                                     downsample=3,
                                     quality=50)

    image_api.retrieve_file_over_http.assert_called_once_with(
        "http://api.brain-map.org/api/v2/section_image_download/126862575"
        "?downsample=3&quality=50",
        path)


def test_api_doc_url_download_section_image_tumor_feature_annotation(image_api):
    path = '126862575.jpg'

    section_image_id = 126862575
    image_api.download_section_image(section_image_id,
                                     downsample=6,
                                     tumor_feature_annotation=True)

    image_api.retrieve_file_over_http.assert_called_once_with(
        "http://api.brain-map.org/api/v2/section_image_download/126862575"
        "?downsample=6&tumor_feature_annotation=true",
        path)


def test_api_doc_url_download_section_image_tumor_feature_annotation_false(image_api):
    path = '126862575.jpg'

    section_image_id = 126862575
    image_api.download_section_image(section_image_id,
                                     downsample=6,
                                     tumor_feature_annotation=False)

    image_api.retrieve_file_over_http.assert_called_once_with(
        "http://api.brain-map.org/api/v2/section_image_download/126862575"
        "?downsample=6&tumor_feature_annotation=false",
        path)


def test_api_doc_url_download_section_image_tumor_feature_boundary(image_api):
    path = '126862575.jpg'

    section_image_id = 126862575
    image_api.download_section_image(section_image_id,
                                     downsample=6,
                                     tumor_feature_boundary=True)

    image_api.retrieve_file_over_http.assert_called_once_with(
        "http://api.brain-map.org/api/v2/section_image_download/126862575"
        "?downsample=6&tumor_feature_boundary=true",
        path)


def test_api_doc_url_download_section_image_tumor_feature_boundary_false(image_api):
    path = '126862575.jpg'

    section_image_id = 126862575
    image_api.download_section_image(section_image_id,
                                     downsample=6,
                                     tumor_feature_boundary=False)

    image_api.retrieve_file_over_http.assert_called_once_with(
        "http://api.brain-map.org/api/v2/section_image_download/126862575"
        "?downsample=6&tumor_feature_boundary=false",
        path)


def test_api_doc_url_download_section_image_expression(image_api):
    path = '126862575.jpg'

    section_image_id = 126862575
    image_api.download_section_image(section_image_id,
                                     downsample=6,
                                     expression=True)

    image_api.retrieve_file_over_http.assert_called_once_with(
        "http://api.brain-map.org/api/v2/section_image_download/126862575"
        "?downsample=6&expression=true",
        path)


def test_api_doc_url_download_section_image_expression_false(image_api):
    path = '126862575.jpg'

    section_image_id = 126862575
    image_api.download_section_image(section_image_id,
                                     downsample=6,
                                     expression=False)

    image_api.retrieve_file_over_http.assert_called_once_with(
        "http://api.brain-map.org/api/v2/section_image_download/126862575"
        "?downsample=6&expression=false",
        path)


def test_api_doc_url_download_atlas_image_downsampled(image_api):
    path = '100883869.jpg'

    section_image_id = 100883869
    image_api.download_atlas_image(section_image_id,
                                   downsample=4)

    image_api.retrieve_file_over_http.assert_called_once_with(
        "http://api.brain-map.org/api/v2/atlas_image_download/100883869"
        "?downsample=4",
        path)


def test_api_doc_url_download_atlas_image_downsampled_low_quality(image_api):
    path = '100883869.jpg'

    section_image_id = 100883869
    image_api.download_atlas_image(section_image_id,
                                   downsample=4,
                                   quality=50)

    image_api.retrieve_file_over_http.assert_called_once_with(
        "http://api.brain-map.org/api/v2/atlas_image_download/100883869"
        "?downsample=4&quality=50",
        path)


def test_api_doc_url_download_atlas_image_annotation(image_api):
    path = '100883869.jpg'

    section_image_id = 100883869
    image_api.download_atlas_image(section_image_id,
                                   downsample=4,
                                   annotation=True)

    image_api.retrieve_file_over_http.assert_called_once_with(
        "http://api.brain-map.org/api/v2/atlas_image_download/100883869"
        "?downsample=4&annotation=true",
        path)


def test_api_doc_url_download_atlas_image_annotation_false(image_api):
    path = '100883869.jpg'

    section_image_id = 100883869
    image_api.download_atlas_image(section_image_id,
                                   downsample=4,
                                   annotation=False)

    image_api.retrieve_file_over_http.assert_called_once_with(
        "http://api.brain-map.org/api/v2/atlas_image_download/100883869"
        "?downsample=4&annotation=false",
        path)


def test_api_doc_url_download_atlas_image_atlas(image_api):
    path = '100883869.jpg'

    section_image_id = 100883869
    image_api.download_atlas_image(section_image_id,
                                   downsample=4,
                                   annotation=True,
                                   atlas=2)

    image_api.retrieve_file_over_http.assert_called_once_with(
        "http://api.brain-map.org/api/v2/atlas_image_download/100883869"
        "?downsample=4&annotation=true&atlas=2",
        path)


def test_api_doc_url_download_atlas_full_resolution_region_of_interest(image_api):
    path = '100883869.jpg'

    subimage_id = 100883869
    image_api.download_atlas_image(subimage_id,
                                   left=6174,
                                   top=2282,
                                   width=1000,
                                   height=1000)

    image_api.retrieve_file_over_http.assert_called_once_with(
        "http://api.brain-map.org/api/v2/atlas_image_download/100883869"
        "?left=6174&top=2282&width=1000&height=1000",
        path)


def test_api_doc_url_download_projection_image_downsampled(image_api):
    path = '126862583.jpg'

    section_image_id = 126862583
    image_api.download_projection_image(section_image_id,
                                        downsample=4)

    image_api.retrieve_file_over_http.assert_called_once_with(
        "http://api.brain-map.org/api/v2/projection_image_download/126862583"
        "?downsample=4",
        path)


def test_api_doc_url_download_projection_image_projection(image_api):
    path = '126862583.jpg'

    section_image_id = 126862583
    image_api.download_projection_image(section_image_id,
                                        downsample=4,
                                        projection=True)

    image_api.retrieve_file_over_http.assert_called_once_with(
        "http://api.brain-map.org/api/v2/projection_image_download/126862583"
        "?downsample=4&projection=true",
        path)


def test_api_doc_url_download_projection_image_projection_false(image_api):
    path = '126862583.jpg'

    section_image_id = 126862583
    image_api.download_projection_image(section_image_id,
                                        downsample=4,
                                        projection=False)

    image_api.retrieve_file_over_http.assert_called_once_with(
        "http://api.brain-map.org/api/v2/projection_image_download/126862583"
        "?downsample=4&projection=false",
        path)


def test_api_doc_url_download_projection_image_view(image_api):
    path = '126862583.jpg'

    section_image_id = 126862583
    image_api.download_projection_image(section_image_id,
                                        downsample=4,
                                        view='projection')

    image_api.retrieve_file_over_http.assert_called_once_with(
        "http://api.brain-map.org/api/v2/projection_image_download/126862583"
        "?downsample=4&view=projection",
        path)


def test_api_doc_url_download_projection_image_view_exception(image_api):
    path = '126862583.jpg'

    section_image_id = 126862583
    
    with pytest.raises(ValueError) as excinfo:
        image_api.download_projection_image(section_image_id,
                                            downsample=4,
                                            view='typo')

    assert excinfo.value.args[0] == "view argument should be 'expression', 'projection', 'tumor_feature_annotation' or 'tumor_feature_boundary'"


def test_api_doc_url_download_image_downsampled(image_api):
    '''
    Notes
    -----
    See: `Image Download Service `<http://help.brain-map.org/display/api/Downloading+an+Image>_
    '''
    path = '69750516.jpg'

    subimage_id = 69750516
    image_api.download_image(subimage_id,
                             downsample=4)

    image_api.retrieve_file_over_http.assert_called_once_with(
        "http://api.brain-map.org/api/v2/image_download/69750516"
        "?downsample=4",
        path)


def test_api_doc_url_download_image_downsampled_low_quality(image_api):
    '''
    Notes
    -----
    See: `Image Download Service `<http://help.brain-map.org/display/api/Downloading+an+Image>_
    '''
    path = '69750516.jpg'

    subimage_id = 69750516
    image_api.download_image(subimage_id,
                             downsample=3,
                             quality=50)

    image_api.retrieve_file_over_http.assert_called_once_with(
        "http://api.brain-map.org/api/v2/image_download/69750516"
        "?downsample=3&quality=50",
        path)


def test_api_doc_url_download_full_resolution_region_of_interest(image_api):
    '''
    Notes
    -----
    See: `Image Download Service `<http://help.brain-map.org/display/api/Downloading+an+Image>_
    '''
    path = '69750516.jpg'

    subimage_id = 69750516
    image_api.download_image(subimage_id,
                             left=6174,
                             top=2282,
                             width=1000,
                             height=1000)

    image_api.retrieve_file_over_http.assert_called_once_with(
        "http://api.brain-map.org/api/v2/image_download/69750516"
        "?left=6174&top=2282&width=1000&height=1000",
        path)


def test_api_doc_url_download_image_expression_mask(image_api):
    '''
    Notes
    -----
    See: `Image Download Service `<http://help.brain-map.org/display/api/Downloading+an+Image>_
    '''
    path = '69750516.jpg'

    subimage_id = 69750516
    image_api.download_image(subimage_id,
                             downsample=4,
                             view='expression')

    image_api.retrieve_file_over_http.assert_called_once_with(
        "http://api.brain-map.org/api/v2/image_download/69750516"
        "?downsample=4&view=expression",
        path)


def test_api_doc_url_download_image_full_resolution(image_api):
    '''
    Notes
    -----
    See: `Experimental Overview and Metadata `<http://help.brain-map.org/display/mouseconnectivity/API#API-ExperimentalOverviewandMetadata>_
    , link labeled 'Download a region of interest at full resolution using default thresholds'.
    '''
    expected = 'http://api.brain-map.org/api/v2/section_image_download/126862575?range=0,932,0,1279,0,4095&left=19045&top=11684&width=1000&height=1000'
    path = '126862575.jpg'

    image_api.retrieve_file_over_http = \
        MagicMock(name='retrieve_file_over_http')

    section_image_id = 126862575
    image_api.download_section_image(section_image_id,
                                     left=19045,
                                     top=11684,
                                     width=1000,
                                     height=1000,
                                     range=[0, 932, 0, 1279, 0, 4095])

    image_api.retrieve_file_over_http.assert_called_once_with(expected, path)


def test_atlas_image_query(image_api):
    expected = "http://api.brain-map.org/api/v2/data/query.json?q=" + \
               "model::Atlas,rma::criteria,[id$eq1]," + \
               "rma::options[only$eqimage_type]," + \
               "pipe::list[type_name$is'image_type']," + \
               "model::AtlasImage,rma::criteria,[annotated$eqtrue]," + \
               "atlas_data_set(atlases[id$eq1])," + \
               "alternate_images[image_type$eq$type_name]," + \
               "rma::options[num_rows$eq'all']" + \
               "[order$eqsub_images.section_number]"

    adult_mouse_atlas_id = 1
    image_api.atlas_image_query(adult_mouse_atlas_id)

    image_api.json_msg_query.assert_called_once_with(expected)


def test_atlas_image_query_image_type_name(image_api):
    expected = "http://api.brain-map.org/api/v2/data/query.json?q=" + \
               "model::AtlasImage,rma::criteria,[annotated$eqtrue]," + \
               "atlas_data_set(atlases[id$eq1])," + \
               "alternate_images[image_type$eq'Atlas - Adult Mouse']," + \
               "rma::options[num_rows$eq'all']" + \
               "[order$eqsub_images.section_number]"

    adult_mouse_atlas_id = 1
    adult_mouse_image_type_name = 'Atlas - Adult Mouse'
    image_api.atlas_image_query(adult_mouse_atlas_id,
                                image_type_name=adult_mouse_image_type_name)

    image_api.json_msg_query.assert_called_once_with(expected)
